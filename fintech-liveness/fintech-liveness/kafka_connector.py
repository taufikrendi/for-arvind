import logging
from django.conf import settings

logger = logging.getLogger(__name__)


def on_delivery(err, msg, obj):
    if err is not None:
        logger.error('Message Funds Service {} delivery failed for user {} with error {}'.format(
            obj.email, obj.email, err))
    else:
        logger.info('Message Funds Service {} successfully produced to {} [{}] at offset {}'.format(
            obj.email, msg.topic(), msg.partition(), msg.offset()))


def commit_completed(err, partitions):
    if err:
        logger.error(str(err))
    else:
        logger.info("Committed Funds Service partition offsets: " + str(partitions))


prod_conf = {
        'bootstrap.servers': settings.KAFKA_SERVER,
        'sasl.mechanism': settings.KAFKA_MECHANISM,
        'security.protocol': settings.KAFKA_SECURITY,
        'sasl.username': settings.KAFKA_USERNAME,
        'sasl.password': settings.KAFKA_PASSWORD,
        'schema.registry.url': settings.SCHEMA_REGISTRY_URL,
        'schema.registry.basic.auth.credentials.source': settings.AUTH_INFO,
        'schema.registry.basic.auth.user.info': settings.AUTH_CREDENTIALS}