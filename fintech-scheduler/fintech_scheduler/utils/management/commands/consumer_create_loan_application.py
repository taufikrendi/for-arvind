import logging
from django.core.management.base import BaseCommand
from loan.consumer.create_loan_application import consumer_create_loan_application

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            while True:
                consumer_create_loan_application()
                self.stdout.write(self.style.SUCCESS('Consumer Create Loan Application Run!'))
        except(TypeError, ValueError, OverflowError):
            logger.info('error base command Create Loan Application ')
            return print('error base command Create Loan Application ')