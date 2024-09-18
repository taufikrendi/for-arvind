import logging
from django.core.management.base import BaseCommand
from account.consumer.ekyc_score import consumer_ekyc_score

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            while True:
                consumer_ekyc_score()
                self.stdout.write(self.style.SUCCESS('Consumer ekyc score Run!'))
        except(TypeError, ValueError, OverflowError):
            logger.info('error base command consumer ekyc score')
            return print('error base command consumer ekyc score')