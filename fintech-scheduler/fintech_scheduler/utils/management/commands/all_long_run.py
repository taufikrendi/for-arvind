from django.core.management.base import BaseCommand

from subprocess import Popen
from sys import stdout, stdin, stderr
import time, os, signal, logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Run all commands'
    commands = [
        # TOKEN MUST BE INTEGRATED WITH KRAKEND and IT'S STILL NOT HAPPEN
        # Account Member
        'python manage.py consumer_create_account', #done
        'python manage.py consumer_profile_filled', #done
        'python manage.py consumer_registered_bank_account', #done
        'python manage.py consumer_selfie_filled', #done
        'python manage.py consumer_set_pin', #done
        'python manage.py consumer_change_pin', #done
        'python manage.py consumer_change_password', #done
        'python manage.py consumer_forgot_password', #done
        # Transaction Member
        'python manage.py consumer_create_transaction', #done
        'python manage.py consumer_proving_transaction', #done
        'python manage.py consumer_create_deposit_time', #done
        # Loan Member
        'python manage.py consumer_create_loan_application', #done
        'python manage.py consumer_update_current_job', #done
        'python manage.py consumer_update_spouse_data',
        # 'python manage.py consumer_update_join_income',
        # 'python manage.py consumer_update_spouse_selfie',
        # Funds Raise
        # 'python manage.py consumer_create_funds_raise',
        # E-KYC SCORE Off Until UAT
        # 'python manage.py consumer_ekyc_score',
        # 'python manage.py produce_ekyc_score',
    ]

    def handle(self, *args, **options):
        global proc_list
        try:
            proc_list = []

            for command in self.commands:
                print("$ " + command)
                proc = Popen(command, shell=True, stdin=stdin, stdout=stdout, stderr=stderr)
                proc_list.append(proc)
            while True:
                logger.info('All Consumer Run!')
                time.sleep(10)
        except KeyboardInterrupt:
            for proc in proc_list:
                logger.error('All Consumer Stop!')
                os.kill(proc.pid, signal.SIGKILL)
