import logging
from django.core.management.base import BaseCommand
from account.consumer.set_pin import consumer_set_pin

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            while True:
                consumer_set_pin()
                self.stdout.write(self.style.SUCCESS('Consumer set pin Run!'))
        except(TypeError, ValueError, OverflowError):
            logger.info('error base command consumer set pin')
            return print('error base command consumer set pin')