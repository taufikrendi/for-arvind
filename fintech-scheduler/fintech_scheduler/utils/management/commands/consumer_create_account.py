import logging
from django.core.management.base import BaseCommand
from account.consumer.registrations import consumer_registrations

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # try:
        # while True:
        consumer_registrations()
            # self.stdout.write(self.style.SUCCESS('Consumer Create Account Run!'))
        # except(TypeError, ValueError, OverflowError):
        #     logger.error('error base command consumer registration')
        #     return print('error base command consumer registration')