import logging, daemon, sys, uuid

from confluent_kafka.avro import AvroConsumer
from confluent_kafka import KafkaError, KafkaException
from kafka_connector import commit_completed

from account.models import AccountMemberVerifyStatus
from excep.exceptions import except_status_500
from utils.models import LogNodeflux

logger = logging.getLogger(__name__)


cons_conf = {
    'bootstrap.servers': 'pkc-ew3qg.asia-southeast2.gcp.confluent.cloud:9092',
    'sasl.mechanism': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': 'BCDCY6SEP7I4MLTW',
    'sasl.password': 'DfxvsdgPN4ytahMDop/YwqbKR0y8vUOzyvtGuyQXZlp4iNwaPqjO+XpQQ915x/GZ',
    'group.id': str(uuid.uuid4()),
    'auto.offset.reset': "smallest",
    'schema.registry.url': 'https://psrc-41vyv.australia-southeast1.gcp.confluent.cloud',
    'schema.registry.basic.auth.credentials.source': 'USER_INFO',
    'schema.registry.basic.auth.user.info': 'VENATWOLOELN3LWG:KDohaIOlmikTW+s7CS1ZK4PBS9+Rs6eUKW42/0BBjGKhCQoQMDnhsoO6fMr5ZZeE',
    'on_commit': commit_completed,
    'session.timeout.ms': 6000,
    'enable.auto.commit': False,
    'reconnect.backoff.max.ms': 5000,
    'debug': 'all',
}


def consumer_ekyc_score():
    global consumer, msg
    try:
        consumer = AvroConsumer(cons_conf)

        consumer.subscribe(['scheduled_get_score'])

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
                    logger.error('Cannot Consume User {}'.format(msg.value()['nik']))
                    raise KafkaException(msg.error())
            else:
                consumer.commit(asynchronous=True)
                AccountMemberVerifyStatus.objects.using('default').\
                    filter(account_member_verify_status_user_nik=msg.value()['nik']).update(
                        account_member_verify_status_dukcapil_score=msg.value()['consume_status_similarity']
                )
                LogNodeflux.objects.using('default').create(
                    log_nodeflux_job_id=msg.value()['id'],
                    log_nodeflux_status=msg.value()['status'],
                    log_nodeflux_analytic_type=msg.value()['analytic_type'],
                    log_nodeflux_message=msg.value()['message'],
                    log_nodeflux_ok=msg.value()['ok'],
                    log_nodeflux_produce=True,
                    log_nodeflux_consume_status_job_id=msg.value()['consume_jobs_id'],
                    log_nodeflux_consume_status_status=msg.value()['consume_status_status'],
                    log_nodeflux_consume_status_analytic_type=msg.value()['consume_status_analytic_type'],
                    log_nodeflux_consume_status_message=msg.value()['consume_status_message'],
                    log_nodeflux_consume_status_ok=msg.value()['consume_status_ok'],
                    log_nodeflux_consume_status=True,
                    log_nodeflux_consume_status_similarity=msg.value()['consume_status_similarity'],
                )
                logger.info('Success Get E-KYC Score for {}'.format(msg.value()['nik']))
    except(TypeError, ValueError, OverflowError):
        logger.info('Consumer {} Get E-KYC Score Failed!'.format(msg.value()['nik']))
        return except_status_500
    finally:
        logger.info('Consumer Stop')
        consumer.close()