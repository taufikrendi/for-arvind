import logging, daemon, sys, uuid

import avro.schema
import avro.io
import io

from confluent_kafka import Consumer

from confluent_kafka import KafkaError, KafkaException
from kafka_connector import commit_completed

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from utils.sender import email_threading

from account.models import AccountLogChangePassword, AccountUserPin
from account.serialize_avro.change_pin import change_pin_schema
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


def consumer_change_pin():
    global consumer, msg, data
    try:
        consumer = Consumer(cons_conf)
        consumer.subscribe(['member-change-pin'])

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
                reader = avro.io.DatumReader(change_pin_schema)
                data = reader.read(decoder)
                AccountUserPin.objects.using('default').filter(account_user_pin_related_user=data['username']) \
                    .update(
                    account_user_pin_data=data['new_pin'],
                    account_user_pin_ip_address=data['ip'],
                    account_user_pin_updated_by=data['username']
                )
                AccountLogChangePassword.objects.create(
                    account_log_change_password_username=data['username'],
                    account_log_change_password_ip_address=data['ip'],
                    account_log_change_password_incoming_from='Change pin menu'
                )
                logger.info('Success Change PIN for {}'.format(data['username']))
                current_site = settings.DOMAIN_CONFIGURATION
                mail_subject = 'Security alert for Changing Password'
                message = render_to_string('registration/front/warning_change_pin.html', {
                    'user': data['username'],
                    'domain': current_site,
                })
                to_email = data['username']
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email_threading(email)
                logger.info('Success Send E-mail Warning Change PIN to User {}'.format(data['username']))

    except(TypeError, ValueError, OverflowError, BufferError):
        logger.error('TypeError, ValueError, OverflowError, BufferError Consumer Change PIN Failed!')
        logger.info('Consumer Change PIN with email {} Failed!'.format(data['username']))
        return except_status_500
    finally:
        logger.error('Consumer Change PIN Stop Before Execute {}'.format(data['username']))
        consumer.close()
