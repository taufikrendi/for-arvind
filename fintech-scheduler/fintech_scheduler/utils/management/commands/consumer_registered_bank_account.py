import logging

from django.core.management.base import BaseCommand
from account.consumer.registered_bank_account import consumer_registered_bank_account

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            while True:
                consumer_registered_bank_account()
                self.stdout.write(self.style.SUCCESS('Consumer register bank account Run!'))
        except(TypeError, ValueError, OverflowError):
            logger.info('error base command consumer register bank account')
            return print('error base command consumer register bank account')