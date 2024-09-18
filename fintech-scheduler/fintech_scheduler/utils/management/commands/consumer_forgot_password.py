import logging

from django.core.management.base import BaseCommand
from account.consumer.forgot_password import consumer_forgot_password

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            while True:
                consumer_forgot_password()
                self.stdout.write(self.style.SUCCESS('Consumer forgot password Run!'))
        except(TypeError, ValueError, OverflowError):
            logger.info('error base command consumer forgot password')
            return print('error base command consumer forgot password')