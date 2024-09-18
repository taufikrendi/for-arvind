import logging, daemon, sys, uuid
import jwt

import avro.schema
import avro.io
import io
from datetime import datetime, timedelta, timezone

from confluent_kafka import Consumer

from confluent_kafka import KafkaError, KafkaException
from kafka_connector import commit_completed

from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.auth.models import User, Group
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from account.models import AccountProfile, AccountBankUsers, AccountPasswordExpired, \
    AccountMemberVerifyStatus, AccountLogResetPassword
from account.serialize_avro.forgot_password import forgot_password_schema
from utils.sender import email_threading
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


def consumer_forgot_password():
    global consumer, msg, data
    try:
        consumer = Consumer(cons_conf)
        consumer.subscribe(['member-forgot-password'])

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
                reader = avro.io.DatumReader(forgot_password_schema)
                data = reader.read(decoder)
                AccountLogResetPassword.objects.using('default').create(
                    account_log_incoming_from='API Forgot Password',
                    account_log_reset_password_email=data['username'],
                    account_log_reset_ip_address=data['ip']
                )
                logger.info('Success Save Forgot Password Data {}'.format(data['username']))
                user = User.objects.using('default_slave').filter(
                    username=data['username'],
                    is_active=True,
                    is_staff=False,
                    is_superuser=False
                )
                if user:
                    current_site = settings.DOMAIN_CONFIGURATION
                    mail_subject = 'Forgot Password'
                    token = jwt.encode({"exp": datetime.now(timezone.utc) + timedelta(days=1), "id":
                        user.values_list("id", flat=True)[0]}, settings.FORGOT_KEY, algorithm="HS256")
                    message = render_to_string('registration/front/reset_password_email.html', {
                        'user': data['username'],
                        'domain': current_site,
                        'uid': urlsafe_base64_encode(force_bytes(data['username'])),
                        'token': token,
                    })
                    to_email = data['username']
                    logger.info(to_email)
                    email = EmailMessage(
                        mail_subject, message, to=[to_email]
                    )
                    logger.info(email)
                    email_threading(email)
                    logger.info('Success Send E-mail Forgot Password to User {}'.format(data['username']))
    except(TypeError, ValueError, OverflowError, BufferError):
        logger.error('TypeError, ValueError, OverflowError, BufferError Forgot Password Failed!')
        logger.info('Consumer Forgot Password with email {} Failed!'.format(data['username']))
        return except_status_500
    finally:
        logger.error('Consumer Forgot Password Stop Before Execute {}'.format(data['username']))
        consumer.close()