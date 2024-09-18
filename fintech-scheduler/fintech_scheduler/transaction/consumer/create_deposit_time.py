import logging, daemon, sys, uuid

import avro.schema
import avro.io
import io
from datetime import datetime

# from confluent_kafka.avro import AvroConsumer
from confluent_kafka import Consumer

from confluent_kafka import KafkaError, KafkaException
from kafka_connector import commit_completed

from deposits.models import DepositProductMaster
from transaction.models import TransactionDepositTimeTransit, TransactionDepositVerified
from transaction.serialize_avro.create_deposit_time import create_deposit_time_schema

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


def consumer_create_deposit_time():
    global consumer, msg, data
    try:
        consumer = Consumer(cons_conf)
        consumer.subscribe(['member-create-deposit-time'])

        while True:
            msg = consumer.poll(timeout=1.0)

            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    logger.error('Kafka Error')
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    logger.error(KafkaException(msg.error()))
            else:
                consumer.commit(asynchronous=True)
                generate = str(uuid.uuid4())
                bytes_reader = io.BytesIO(msg.value())
                decoder = avro.io.BinaryDecoder(bytes_reader)
                reader = avro.io.DatumReader(create_deposit_time_schema)
                data = reader.read(decoder)
                get_data = DepositProductMaster.objects.using('funds_slave').filter(
                    deposit_product_master_id=data['product_type'],
                )
                TransactionDepositTimeTransit.objects.using('transaction_master').create(
                    transaction_deposit_time_transit_user_related=data['email'],
                    transaction_deposit_time_transit_code=generate,
                    transaction_deposit_time_transit_product_type=data['product_type'],
                    transaction_deposit_time_transit_amount=data['amount'],
                    transaction_deposit_time_transit_period_base=data['period_base'],
                    transaction_deposit_time_transit_type='Deposito',
                    transaction_deposit_time_revenue_share=get_data.values_list(
                        'deposit_product_master_revenue_share', flat=True).first(),
                    transaction_deposit_time_fluctuate_revenue=get_data.values_list(
                        'deposit_product_minimum_fluctuate_revenue', flat=True).first(),
                    transaction_deposit_time_transit_created_by=data['email']
                )
                TransactionDepositVerified.objects.using('transaction_master').create(
                    transaction_deposit_verified_user_related=data['email'],
                    transaction_deposit_verified_transit_code=generate,
                    transaction_deposit_verified_created_by=data['email'],
                    transaction_deposit_verified_status=data['payment_with'],
                )
                logger.info('Success Member Deposit Period for {}'.format(data['email']))

    except(TypeError, ValueError, OverflowError, BufferError):
        logger.error('TypeError, ValueError, OverflowError, BufferError Consumer Create Member Deposit Period Failed!')
        logger.info('Consumer Create Member Deposit Period with email {} Failed!'.format(data['email']))
        return except_status_500
    finally:
        logger.error('Consumer Create Member Deposit Period Stop Before Execute {}'.format(data['email']))
        consumer.close()