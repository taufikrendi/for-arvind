import logging
from django.core.management.base import BaseCommand
from transaction.consumer.create_transaction import consumer_create_transaction

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            while True:
                logger.info('Consumer create transaction Run!')
                consumer_create_transaction()
                logger.error('Consumer create transaction Stop Run!')
        except(TypeError, ValueError, OverflowError):
            logger.info('error base command consumer create transaction')
            return print('error base command consumer create transaction')