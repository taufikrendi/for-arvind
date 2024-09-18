import logging
from django.core.management.base import BaseCommand
from account.consumer.selfie_filled import consumer_selfie_filled

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            while True:
                consumer_selfie_filled()
                self.stdout.write(self.style.SUCCESS('Consumer Selfie Filled Run!'))
        except(TypeError, ValueError, OverflowError):
            logger.info('error base command consumer Selfie Filled')
            return print('error base command consumer Selfie Filled')