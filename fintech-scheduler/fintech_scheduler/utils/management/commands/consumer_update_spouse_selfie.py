import logging
from django.core.management.base import BaseCommand
from loan.consumer.update_spouse_selfie import consumer_update_spouse_selfie

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            while True:
                consumer_update_spouse_selfie()
                self.stdout.write(self.style.SUCCESS('Consumer Update Spouse Selfie Job Run!'))
        except(TypeError, ValueError, OverflowError):
            logger.info('error base command Consumer Update Spouse Selfie Job')
            return print('error base command Consumer Update Spouse Selfie Job')