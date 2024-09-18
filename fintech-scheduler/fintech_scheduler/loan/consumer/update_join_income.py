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
from loan.serialize_avro.update_join_income_data import update_join_income_schema
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


def consumer_update_join_income():
    global consumer, msg, data
    try:
        consumer = Consumer(cons_conf)
        consumer.subscribe(['update-join-income'])

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
                reader = avro.io.DatumReader(update_join_income_schema)
                data = reader.read(decoder)
                LoanApplicationSpouseProfile.objects.using('funds_master').filter(
                    loan_application_spouse_profile_user_related=data['email'],
                ).update(
                    loan_application_spouse_profile_join_income=data['join_income'],
                    loan_application_spouse_profile_company_name=data['company_name'],
                    loan_application_spouse_profile_company_phone=data['company_phone'],
                    loan_application_spouse_profile_company_address_prov=data['company_address_prov'],
                    loan_application_spouse_profile_company_address_district=data['company_address_district'],
                    loan_application_spouse_profile_company_address_sub_district=data['company_address_sub_district'],
                    loan_application_spouse_profile_company_address=data['company_address'],
                    loan_application_spouse_profile_company_postal_code=data['company_postal_code'],
                    loan_application_spouse_profile_company_establish_from=data['company_establish_from'],
                    loan_application_spouse_profile_company_category=data['company_category'],
                    loan_application_spouse_profile_job_started_date=data['job_started_date'],
                    loan_application_spouse_profile_job_status=data['job_status'],
                    loan_application_spouse_profile_job_evident=data['job_evident'],
                    loan_application_spouse_profile_salary=data['salary'],
                    loan_application_spouse_profile_placement=data['placement'],
                    loan_application_spouse_profile_created_by_job=data['email'],
                    loan_application_spouse_profile_created_date_job=datetime.now
                )
                logger.info('Success Update Join Income Data {}'.format(data['email']))
    except(TypeError, ValueError, OverflowError, BufferError):
        logger.error('TypeError, ValueError, OverflowError, BufferError Consumer Update Join Income Failed!')
        logger.info('Consumer Update Join Income with email {} Failed!'.format(data['email']))
        return except_status_500
    finally:
        logger.error('Consumer Update Join Income Stop Before Execute {}'.format(data['email']))
        consumer.close()