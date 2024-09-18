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

from account.models import AccountBankUsers, AccountMemberVerifyStatus
from account.serialize_avro.registered_bank_account import registered_bank_account_schema
from deposits.models import DepositMemberMandatory, DepositMemberPrincipal
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

def consumer_registered_bank_account():
    global consumer, msg, data
    try:
        consumer = Consumer(cons_conf)

        consumer.subscribe(['member-register-account-bank'])

        while True:
            msg = consumer.poll(timeout=1.0)

            if msg is None:
                continue

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
                reader = avro.io.DatumReader(registered_bank_account_schema)
                data = reader.read(decoder)
                check = DepositMemberPrincipal.objects.using('funds_slave').filter(
                    deposit_member_principal_user_related=data['username'],
                )
                check_2 = DepositMemberMandatory.objects.using('funds_slave').filter(
                    deposit_member_mandatory_user_related=data['username'],
                )
                check_3 = AccountBankUsers.objects.using('default_slave').filter(
                    account_bank_user_related_to_user=data['username'],
                )
                if check or check_2 or check_3:
                    continue
                else:
                    AccountBankUsers.objects.using('default').create(
                        account_bank_user_name=data['holder_name'],
                        account_bank_user_number=data['holder_number'],
                        account_bank_user_related_to_bank=data['holder_bank_code'],
                        account_bank_user_related_to_user=data['username'],
                        account_bank_user_created_by=data['username']
                    )
                    AccountMemberVerifyStatus.objects.using('default').filter(
                        account_member_verify_status_user_related=data['username'],
                    ).update(
                        account_member_verify_status_bank=True,
                        account_member_verify_status_bank_filled_date=datetime.now()
                    )
                    DepositMemberPrincipal.objects.using('funds_master').create(
                        deposit_member_principal_user_related=data['username'],
                        deposit_member_principal_created_by=data['username'],
                    )
                    DepositMemberMandatory.objects.using('funds_master').create(
                        deposit_member_mandatory_user_related=data['username'],
                        deposit_member_mandatory_created_by=data['username']
                    )
                    logger.info('Success Save Registered Bank Account Data {}'.format(data['username']))
    except(TypeError, ValueError, OverflowError, BufferError):
        logger.error('TypeError, ValueError, OverflowError, BufferError Consumer Registered Bank Account Failed!')
        logger.info('Consumer Registered Bank Account with email {} Failed!'.format(data['username']))
        return except_status_500
    finally:
        logger.error('Consumer Registered Bank Account Stop Before Execute {}'.format(data['username']))
        consumer.close()