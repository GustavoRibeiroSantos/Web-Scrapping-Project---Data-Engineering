from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.utils import timezone
from django_apscheduler.models import DjangoJobExecution
import sys
from BookClub.models import Model 

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    # run this job every 24 hours
    scheduler.add_job(Model.web_scraper, 'interval', hours=24)
    register_events(scheduler)
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)