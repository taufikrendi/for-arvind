import logging, daemon, sys, uuid

import avro.schema
import avro.io
import io
from datetime import datetime

# from confluent_kafka.avro import AvroConsumer
from confluent_kafka import Consumer

from confluent_kafka import KafkaError, KafkaException
from kafka_connector import commit_completed

from loan.models import LoanApplication, LoanCreditScore, LoanApplicationVerification, \
    LoanAppraisalCollateral, LoanApproval
from loan.serialize_avro.create_loan_application import create_loan_application_schema
from excep.exceptions import except_status_500

logger = logging.getLogger(__name__)


cons_conf = {
    'bootstrap.servers': 'dokaf_kafka_1:9092',
    'sasl.mechanism': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': 'BCDCY6SEP7I4MLTW',
    'sasl.password': 'DfxvsdgPN4ytahMDop/YwqbKR0y8vUOzyvtGuyQXZlp4iNwaPqjO+XpQQ915x/GZ',
    'schema.registry.url': 'https://psrc-41vyv.australia-southeast1.gcp.confluent.cloud',
    'schema.registry.basic.auth.credentials.source': 'USER_INFO',
    'schema.registry.basic.auth.user.info': 'VENATWOLOELN3LWG:KDohaIOlmikTW+s7CS1ZK4PBS9+Rs6eUKW42/0BBjGKhCQoQMDnhsoO6fMr5ZZeE',
    'group.id':  str(uuid.uuid4()),
    'auto.offset.reset': "latest",
    'on_commit': commit_completed,
    'session.timeout.ms': 6000,
    'enable.auto.commit': 'false',
    'reconnect.backoff.max.ms': 5000,
    'debug': 'all',
}


def consumer_create_loan_application():
    global consumer, msg, data
    try:
        consumer = Consumer(cons_conf)
        consumer.subscribe(['member-create-loan-application'])

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
                generate = str(uuid.uuid4())
                bytes_reader = io.BytesIO(msg.value())
                decoder = avro.io.BinaryDecoder(bytes_reader)
                reader = avro.io.DatumReader(create_loan_application_schema)
                data = reader.read(decoder)
                LoanApplication.objects.using('funds_master').create(
                    loan_application_user_related=data['email'],
                    loan_application_code_related=generate,
                    loan_application_type_usage=data['type_usage'],
                    loan_application_amount=data['amount'],
                    loan_application_installment_month=data['installment_month'],
                    loan_application_reason=data['reason'],
                    loan_application_collateral=data['collateral'],
                    loan_application_collateral_evident=data['proving_collateral'],
                    loan_application_link_url=data['url'],
                    loan_application_create_by=data['email'],
                )
                LoanApplicationVerification.objects.using('funds_master').create(
                    loan_application_verification_user_related=data['email'],
                    loan_application_verification_related_loan=generate,
                )
                LoanCreditScore.objects.using('funds_master').create(
                    loan_credit_score_user_related=data['email'],
                    loan_credit_score_application_code_related=generate
                )
                LoanAppraisalCollateral.objects.using('funds_master').create(
                    loan_appraisal_collateral_user_related=data['email'],
                    loan_appraisal_collateral_related_loan=generate,
                )
                LoanApproval.objects.using('funds_master').create(
                    loan_approval_user_related=data['email'],
                    loan_approval_related_loan=generate,
                    loan_approval_status='On Manual Verify'
                )
                logger.info('Success Create Loan Application {}'.format(data['email']))
    except(TypeError, ValueError, OverflowError, BufferError):
        logger.error('TypeError, ValueError, OverflowError, BufferError Consumer Create Loan Application Failed!')
        logger.info('Consumer Create Loan Application with email {} Failed!'.format(data['email']))
        return except_status_500
    finally:
        logger.error('Consumer Create Loan Application Stop Before Execute {}'.format(data['email']))
        consumer.close()