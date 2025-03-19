import schedule
import time
from .utils import fetch_noaa_data
from celery import shared_task

@shared_task
def run_scheduler():
    schedule.every(1).minutes.do(fetch_noaa_data)
    while True:
        schedule.run_pending()
        time.sleep(1)

import threading
threading.Thread(target=run_scheduler, daemon=True).start()
