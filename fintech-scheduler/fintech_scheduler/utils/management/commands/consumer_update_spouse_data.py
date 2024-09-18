import logging
from django.core.management.base import BaseCommand
from loan.consumer.update_spouse_data import consumer_update_spouse_data

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            while True:
                consumer_update_spouse_data()
                self.stdout.write(self.style.SUCCESS('Consumer Update Spouse Data Run!'))
        except(TypeError, ValueError, OverflowError):
            logger.info('error base command Consumer Update Spouse Data Job ')
            return print('error base command Consumer Update Spouse Data Job')