from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')

app = Celery('django_celery_project')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
# app.conf.beat_schedule = {
#     'send-mail-every-day-at-8': {
#         'task': 'send_mail_app.tasks.send_mail_func',
#         # 'schedule': crontab(hour=4, minute=39,day_of_month=19,month_of_year=6),
#         'schedule': crontab(hour=0, minute=2),
#         #'args': (2,)
#     }
    
# }

app.conf.beat_schedule = {
'Send_mail_to_Client': {
'task': 'mainapp.views.schedule_mail',
# 'schedule': 30.0, #every 30 seconds it will be called
'schedule': crontab(minute=2),
#'args': (2,) you can pass arguments also if rquired
}
}



# Celery Schedules - https://docs.celeryproject.org/en/stable/reference/celery.schedules.html
app.conf.beat_scheduler='django_celery_beat.schedulers.DatabaseScheduler'

app.autodiscover_tasks(settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')