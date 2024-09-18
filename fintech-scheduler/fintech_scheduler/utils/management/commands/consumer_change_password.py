import logging
from django.core.management.base import BaseCommand
from account.consumer.change_password import consumer_change_password

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            while True:
                consumer_change_password()
                self.stdout.write(self.style.SUCCESS('Consumer change password Run!'))
        except(TypeError, ValueError, OverflowError):
            logger.info('error base command consumer change password')
            return print('error base command consumer change password')