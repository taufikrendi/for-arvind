import logging
from django.conf import settings

logger = logging.getLogger(__name__)


def on_delivery(err, msg, obj):
    if err is not None:
        logger.error('Message Account Service {} delivery failed for user {} with error {}'.format(
            obj.email, obj.email, err))
    else:
        logger.info('Message Account Service {} successfully produced to {} [{}] at offset {}'.format(
            obj.email, msg.topic(), msg.partition(), msg.offset()))


def commit_completed(err, partitions):
    if err:
        logger.error(str(err))
    else:
        logger.info("Committed Account Service partition offsets: " + str(partitions))


prod_conf = {
        'bootstrap.servers': settings.KAFKA_SERVER,
        "retry.backoff.ms": 3000,
        "retries": 3,
        "default.topic.config": {
            "request.required.acks": "all",
            "delivery.report.only.error": True,
        },
        "max.in.flight.requests.per.connection": 1,
        "queue.buffering.max.messages": 100000,
        "queue.buffering.max.ms": 0,
        "batch.num.messages": 50,
        "message.max.bytes": 2000000,
        # 'sasl.mechanism': settings.KAFKA_MECHANISM,
        # 'broker.address.family': 'v4',
        # 'security.protocol': settings.KAFKA_SECURITY,
        # 'sasl.username': settings.KAFKA_USERNAME,
        # 'sasl.password': settings.KAFKA_PASSWORD,
        # 'schema.registry.url': settings.SCHEMA_REGISTRY_URL,
        # 'debug': 'all',
        # 'schema.registry.basic.auth.credentials.source': settings.AUTH_INFO,
        # 'schema.registry.basic.auth.user.info': settings.AUTH_CREDENTIALS
}