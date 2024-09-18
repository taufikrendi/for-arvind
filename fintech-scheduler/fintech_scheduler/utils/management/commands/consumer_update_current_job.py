import logging
from django.core.management.base import BaseCommand
from loan.consumer.update_current_job import consumer_update_current_job

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            while True:
                consumer_update_current_job()
                self.stdout.write(self.style.SUCCESS('Consumer Update Current Job Run!'))
        except(TypeError, ValueError, OverflowError):
            logger.info('error base command Consumer Update Current Job ')
            return print('error base command Consumer Update Current Job')