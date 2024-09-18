import logging, daemon, sys, uuid

import avro.schema
import avro.io
import io
from datetime import datetime

# from confluent_kafka.avro import AvroConsumer
from confluent_kafka import Consumer

from confluent_kafka import KafkaError, KafkaException
from kafka_connector import commit_completed

from loan.models import LoanCurrentJobs
from loan.serialize_avro.update_current_jobs import update_current_job_schema
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


def consumer_update_current_job():
    global consumer, msg, data
    try:
        consumer = Consumer(cons_conf)
        consumer.subscribe(['update-current-jobs'])

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
                reader = avro.io.DatumReader(update_current_job_schema)
                data = reader.read(decoder)
                LoanCurrentJobs.objects.using('funds_master').create(
                    loan_current_jobs_user_related=data['email'],
                    loan_current_jobs_code_related=data['code'],
                    loan_current_jobs_company_name=data['company_name'],
                    loan_current_jobs_company_phone=data['company_phone'],
                    loan_current_jobs_company_address_prov=data['company_address_prov'],
                    loan_current_jobs_company_address_district=data['company_address_dist'],
                    loan_current_jobs_company_address_sub_district=data['company_address_sub_dist'],
                    loan_current_jobs_company_address=data['company_address'],
                    loan_current_jobs_company_postal_code=data['company_address_postal_code'],
                    loan_current_jobs_company_establish_from=data['company_establish_from'],
                    loan_current_jobs_company_category=data['company_unit_category'],
                    loan_current_jobs_started_date=data['jobs_started_date'],
                    loan_current_jobs_status=data['jobs_status'],
                    loan_current_jobs_salary=data['jobs_salary'],
                    loan_current_jobs_placement=data['jobs_placement'],
                    loan_current_jobs_evident=data['jobs_evident'],
                    loan_current_jobs_created_by=data['email'],
                )
                logger.info('Success Update Current Jobs {}'.format(data['email']))
    except(TypeError, ValueError, OverflowError, BufferError):
        logger.error('TypeError, ValueError, OverflowError, BufferError Consumer Update Current Jobs Failed!')
        logger.info('Consumer Update Current Jobs with email {} Failed!'.format(data['email']))
        return except_status_500
    finally:
        logger.error('Consumer Update Current Jobs Stop Before Execute {}'.format(data['email']))
        consumer.close()