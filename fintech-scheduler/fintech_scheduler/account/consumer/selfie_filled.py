import logging, daemon, sys, uuid

import avro.schema
import avro.io
import io

from confluent_kafka import Consumer

from confluent_kafka import KafkaError, KafkaException
from kafka_connector import commit_completed

from account.models import AccountProfile, AccountReplicationProfile
from account.serialize_avro.selfie_filled import selfie_filled_schema
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


def consumer_selfie_filled():
    global consumer, msg, data
    try:
        consumer = Consumer(cons_conf)
        consumer.subscribe(['member-selfie-filled'])

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
                bytes_reader = io.BytesIO(msg.value())
                decoder = avro.io.BinaryDecoder(bytes_reader)
                reader = avro.io.DatumReader(selfie_filled_schema)
                data = reader.read(decoder)
                AccountProfile.objects.using('default').filter(
                    account_profile_user_related=data['username']
                ).update(
                    account_profile_selfie=data['selfie'],
                    account_profile_selfie_eidentity=data['selfie_ektp'],
                    account_profile_eidentity=data['ektp'],
                    account_profile_enpwp=data['enpwp']
                )
                AccountReplicationProfile.objects.using('default').create(
                    account_replication_profile_selfie=data['selfie'],
                    account_replication_profile_selfie_eidentity=data['selfie_ektp'],
                    account_replication_profile_eidentity=data['ektp'],
                    account_replication_profile_enpwp=data['enpwp'],
                )
                logger.info('Success Save Selfie {}'.format(data['username']))
    except(TypeError, ValueError, OverflowError, BufferError):
        logger.error('TypeError, ValueError, OverflowError, BufferError Consumer Selfie Failed!')
        logger.info('Consumer Selfie with email {} Failed!'.format(data['username']))
        return except_status_500
    finally:
        logger.error('Consumer Selfie Stop Before Execute {}'.format(data['username']))
        consumer.close()
