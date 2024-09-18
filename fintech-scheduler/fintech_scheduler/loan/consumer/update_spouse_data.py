import logging, daemon, sys, uuid

import avro.schema
import avro.io
import io
from datetime import datetime

# from confluent_kafka.avro import AvroConsumer
from confluent_kafka import Consumer

from confluent_kafka import KafkaError, KafkaException
from kafka_connector import commit_completed

from loan.models import LoanApplicationSpouseProfile
from loan.serialize_avro.update_spouse_data import update_spouse_data_schema
from excep.exceptions import except_status_500
from utils.validators import str2bool

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


def consumer_update_spouse_data():
    global consumer, msg, data
    try:
        consumer = Consumer(cons_conf)
        consumer.subscribe(['update-spouse-data'])

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
                reader = avro.io.DatumReader(update_spouse_data_schema)
                data = reader.read(decoder)
                LoanApplicationSpouseProfile.objects.using('funds_master').create(
                    loan_application_spouse_profile_user_related=data['email'],
                    loan_application_spouse_profile_code_related=data['code'],
                    loan_application_spouse_profile_guarantor=str2bool(data['guarantor']),
                    loan_application_spouse_profile_full_name=data['full_name'],
                    loan_application_spouse_profile_status=data['status'],
                    loan_application_spouse_profile_dob=data['dob'],
                    loan_application_spouse_profile_pob=data['pob'],
                    loan_application_spouse_profile_address=data['address'],
                    loan_application_spouse_profile_province=data['province'],
                    loan_application_spouse_profile_district=data['district'],
                    loan_application_spouse_profile_sub_district=data['sub_district'],
                    loan_application_spouse_profile_postal_code=data['postal_code'],
                    loan_application_spouse_profile_phone_number=data['phone_number'],
                    loan_application_spouse_profile_created_by=data['email']
                )
                logger.info('Success Update Spouse Data {}'.format(data['email']))
    except(TypeError, ValueError, OverflowError, BufferError):
        logger.error('TypeError, ValueError, OverflowError, BufferError Consumer Update Spouse Failed!')
        logger.info('Consumer Update Spouse with email {} Failed!'.format(data['email']))
        return except_status_500
    finally:
        logger.error('Consumer Update Spouse Stop Before Execute {}'.format(data['email']))
        consumer.close()