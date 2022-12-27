import os
from celery import Celery
# from django.conf import settings
from celery.schedules import crontab
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fbclone.settings.dev')

app = Celery('fbclone')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes. 
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.conf.beat_schedule = {
    'send-mail-every-day-at': {
        'task': 'login.task.send_mail_task',
        # 'schedule': crontab(hour=0, minute=46, day_of_month=19, month_of_year = 6),
        'schedule': crontab(hour=15, minute=46),
        # 'schedule': 10,
        #'args': (2,)
    }
    
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
