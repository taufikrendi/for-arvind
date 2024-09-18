import logging, daemon, uuid, sys

import avro.schema
import avro.io
import io

from confluent_kafka import Consumer

from confluent_kafka import KafkaError, KafkaException
from kafka_connector import commit_completed

from transaction.models import TransactionDepositTransit, TransactionDepositVerified
from transaction.serialize_avro.create_transactions import create_transactions_schema
from excep.exceptions import except_status_500

logger = logging.getLogger(__name__)


cons_conf = {
    'bootstrap.servers': 'dokaf_kafka_1:9092',
    # 'sasl.mechanism': 'PLAIN',
    # 'security.protocol': 'SASL_SSL',
    # 'sasl.username': 'BCDCY6SEP7I4MLTW',
    # 'sasl.password': 'DfxvsdgPN4ytahMDop/YwqbKR0y8vUOzyvtGuyQXZlp4iNwaPqjO+XpQQ915x/GZ',
    # 'schema.registry.url': 'https://psrc-41vyv.australia-southeast1.gcp.confluent.cloud',
    # 'schema.registry.basic.auth.credentials.source': 'USER_INFO',
    # 'schema.registry.basic.auth.user.info': 'VENATWOLOELN3LWG:KDohaIOlmikTW+s7CS1ZK4PBS9+Rs6eUKW42/0BBjGKhCQoQMDnhsoO6fMr5ZZeE',
    'group.id':  str(uuid.uuid4()),
    'auto.offset.reset': "latest",
    'on_commit': commit_completed,
    'session.timeout.ms': 6000,
    'enable.auto.commit': 'false',
    'reconnect.backoff.max.ms': 5000,
    'debug': 'all',
}


def consumer_create_transaction():
    global consumer, msg, data
    try:
        consumer = Consumer(cons_conf)
        consumer.subscribe(['member-create-trans'])

        while True:
            msg = consumer.poll(timeout=1.0)

            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    logger.error(
                        'KAFKA ERROR - %% %s [%d] reached end at offset %d\n' %
                        (msg.topic(), msg.partition(), msg.offset()))
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    logger.error(KafkaException(msg.error()))
            else:
                consumer.commit(asynchronous=True)
                generate = str(uuid.uuid4())
                bytes_reader = io.BytesIO(msg.value())
                decoder = avro.io.BinaryDecoder(bytes_reader)
                reader = avro.io.DatumReader(create_transactions_schema)
                data = reader.read(decoder)

                TransactionDepositTransit.objects.using('transaction_master').create(
                    transaction_deposit_transit_code=generate,
                    transaction_deposit_transit_user_related=data['username'],
                    transaction_deposit_transit_amount=data['amount'],
                    transaction_deposit_transit_unique_code_amount=data['unique_code'],
                    transaction_deposit_transit_gt_amount=data['amount']+data['unique_code'],
                    transaction_deposit_transit_type='Credit',
                    transaction_deposit_transit_created_by=data['username'],
                )
                TransactionDepositVerified.objects.using('transaction_master').create(
                    transaction_deposit_verified_user_related=data['username'],
                    transaction_deposit_verified_transit_code=generate,
                    transaction_deposit_verified_created_by=data['username'],
                    transaction_deposit_verified_status=data['payment_with'],
                )
                logger.info('Success Create Transactions for {}'.format(data['username']))
    except(TypeError, ValueError, OverflowError, BufferError):
        logger.error('TypeError, ValueError, OverflowError, BufferError Consumer Create Transactions Failed!')
        logger.info('Consumer Create Transactions with email {} Failed!'.format(data['username']))
        return except_status_500
    finally:
        logger.error('Consumer Create Transactions Stop Before Execute {}'.format(data['username']))
        consumer.close()