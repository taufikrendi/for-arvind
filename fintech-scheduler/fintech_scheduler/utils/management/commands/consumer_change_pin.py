import logging
from django.core.management.base import BaseCommand
from account.consumer.change_pin import consumer_change_pin

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            while True:
                consumer_change_pin()
                self.stdout.write(self.style.SUCCESS('Consumer change pin Run!'))
        except(TypeError, ValueError, OverflowError):
            logger.info('error base command consumer change pin')
            return print('error base command consumer change pin')