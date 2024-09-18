import logging, daemon, sys, uuid

import avro.schema
import avro.io
import io
from datetime import datetime

from confluent_kafka import Consumer

from confluent_kafka import KafkaError, KafkaException
from kafka_connector import commit_completed

from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.auth.models import User, Group
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from account.models import AccountProfile, AccountBankUsers, AccountPasswordExpired, \
    AccountMemberVerifyStatus, AccountLogResetPassword
from account.serialize_avro.registrations import registration_schema
from utils.sender import email_threading
from utils.validators import str2bool
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


def consumer_registrations():
    global consumer, msg, data
    try:
        consumer = Consumer(cons_conf)
        consumer.subscribe(['member-registrations'])

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
                reader = avro.io.DatumReader(registration_schema)
                data = reader.read(decoder)
                check = User.objects.using('default_slave').filter(username=data['email'])
                if not check:
                    user = User.objects.using('default').create(
                        username=data['email'],
                        email=data['email'],
                        first_name=data['first_name'],
                        password=data['password'],
                        is_superuser=False,
                        is_staff=False,
                        is_active=False,
                        last_login=datetime.now()
                    )
                    AccountProfile.objects.using('default').create(
                        account_profile_user_related=data['email'],
                        account_profile_phone_number=data['phone_number'],
                        account_profile_created_by=data['email']
                    )
                    AccountPasswordExpired.objects.using('default').create(
                        account_password_expired_user_related=data['email'],
                        account_password_expired_update_by=data['email'],
                    )
                    AccountMemberVerifyStatus.objects.using('default').create(
                        account_member_verify_status_user_related=data['email'],
                        account_member_verify_status_subscriber_agreement=str2bool(data['agreement']),
                        account_member_verify_status_created_by=data['email']
                    )
                    new_group = Group.objects.get(name='Member')
                    user.groups.add(new_group)
                    logger.info('Success Created User {}'.format(data['email']))
                    current_site = settings.DOMAIN_CONFIGURATION
                    mail_subject = 'Activate your account.'
                    message = render_to_string('registration/front/activation_email.html', {
                        'user': data['email'],
                        'domain': current_site,
                        'uid': urlsafe_base64_encode(force_bytes(data['email'])),
                        'token': default_token_generator.make_token(user),
                    })
                    to_email = data['email']
                    email = EmailMessage(
                        mail_subject, message, to=[to_email]
                    )
                    email_threading(email)
                    logger.info('Success Send E-mail Registration to User {}'.format(data['email']))
    except(TypeError, ValueError, OverflowError, BufferError):
        logger.error('TypeError, ValueError, OverflowError, BufferError Consumer Customer Registrations Failed!')
        logger.info('Consumer Customer Registrations with email {} Failed!'.format(data['email']))
        return except_status_500
    finally:
        logger.error('Consumer Customer Registrations Stop Before Execute {}'.format(data['email']))
        consumer.close()




