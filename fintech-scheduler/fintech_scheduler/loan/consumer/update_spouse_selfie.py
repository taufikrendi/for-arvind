import logging, daemon, sys, uuid

import avro.schema
import avro.io
import io
from datetime import datetime

# from confluent_kafka.avro import AvroConsumer
from confluent_kafka import Consumer

from confluent_kafka import KafkaError, KafkaException
from datetime import datetime
from kafka_connector import commit_completed

from loan.models import LoanApplicationSpouseProfile
from loan.serialize_avro.update_spouse_selfie_data import update_spouse_selfie_data_schema
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


def consumer_update_spouse_selfie():
    global consumer, msg, data
    try:
        consumer = Consumer(cons_conf)
        consumer.subscribe(['update-spouse-selfie'])

        while True:
            msg = consumer.poll()

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
                bytes_reader = io.BytesIO(msg.value())
                decoder = avro.io.BinaryDecoder(bytes_reader)
                reader = avro.io.DatumReader(update_spouse_selfie_data_schema)
                data = reader.read(decoder)
                LoanApplicationSpouseProfile.objects.using('funds_master').filter(
                    loan_application_spouse_profile_user_related=data['email'],
                ).create(
                    loan_application_spouse_profile_selfie=data['selfie'],
                    loan_application_spouse_profile_selfie_eidentity=data['selfie_eidentity'],
                    loan_application_spouse_profile_eidentity=data['eidentity'],
                    loan_application_spouse_profile_enpwp=data['enpwp'],
                    loan_application_spouse_profile_family_card=data['family_card'],
                    loan_application_spouse_marriage_certificate=data['marriage_certificate'],
                    loan_application_spouse_profile_created_by_selfie=data['email'],
                    loan_application_spouse_profile_created_date_selfie=datetime.now()
                )
                logger.info('Success Update Spouse Selfie {}'.format(data['email']))
    except(TypeError, ValueError, OverflowError, BufferError):
        logger.error('TypeError, ValueError, OverflowError, BufferError Consumer Update Spouse Selfie Failed!')
        logger.info('Consumer Update Spouse Selfie with email {} Failed!'.format(data['email']))
        return except_status_500
    finally:
        logger.error('Consumer Update Spouse Selfie Stop Before Execute {}'.format(data['email']))
        consumer.close()