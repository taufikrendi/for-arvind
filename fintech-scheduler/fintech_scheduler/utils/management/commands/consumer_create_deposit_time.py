import logging
from django.core.management.base import BaseCommand
from transaction.consumer.create_deposit_time import consumer_create_deposit_time

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            while True:
                consumer_create_deposit_time()
                self.stdout.write(self.style.SUCCESS('Consumer Deposit Period Run!'))
        except(TypeError, ValueError, OverflowError):
            logger.info('error base command consumer Deposit Period')
            return print('error base command consumer Deposit Period')