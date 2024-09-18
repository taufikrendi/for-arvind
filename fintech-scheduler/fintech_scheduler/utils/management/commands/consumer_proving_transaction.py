import logging
from django.core.management.base import BaseCommand
from transaction.consumer.proving_transaction import consumer_proving_transaction

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            while True:
                consumer_proving_transaction()
                self.stdout.write(self.style.SUCCESS('Consumer proving transaction Run!'))
        except(TypeError, ValueError, OverflowError):
            logger.info('error base command consumer proving transaction')
            return print('error base command consumer proving transaction')