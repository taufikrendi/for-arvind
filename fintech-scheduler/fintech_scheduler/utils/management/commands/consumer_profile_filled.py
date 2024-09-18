import logging

from django.core.management.base import BaseCommand
from account.consumer.profile_filled import consumer_profile_filled

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            while True:
                consumer_profile_filled()
                self.stdout.write(self.style.SUCCESS('Consumer profile filled Run!'))
        except(TypeError, ValueError, OverflowError):
            logger.info('error base command consumer profile filled')
            return print('error base command consumer profile filled')