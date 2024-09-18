import schedule, time, logging

from django.core.management.base import BaseCommand
from utils.continuous import run_continuously
from account.produce.get_ekyc_results import nodeflux_produce_get_result

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            schedule.every(0.1).second.do(nodeflux_produce_get_result)
            stop_run_continuously = run_continuously()
            time.sleep(4)
            stop_run_continuously.set()

            while True:
                schedule.run_pending()
                time.sleep(1)
        except(TypeError, ValueError, OverflowError):
            logger.info('error base command long run scheduler for produce ekcy score')
            return print('error base command long run scheduler for produce ekcy score')