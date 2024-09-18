import logging
from django.core.management.base import BaseCommand
from loan.consumer.update_join_income import consumer_update_join_income

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            while True:
                consumer_update_join_income()
                self.stdout.write(self.style.SUCCESS('Consumer Update Join Income Run!'))
        except(TypeError, ValueError, OverflowError):
            logger.info('error base command Consumer Update Join Income')
            return print('error base command Consumer Update Join Income')