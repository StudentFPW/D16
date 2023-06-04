import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'D16.settings')

app = Celery('D16')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# FIXME
app.conf.beat_schedule = {
    'print_every_5_seconds': {
        'task': 'CRON.tasks.printer',
        'schedule': 5,
        'args': (5,),
    },
}

# FIXME
app.conf.beat_schedule = {
    'print_every_5_seconds': {
        'task': 'CRON.tasks.hello',
        'schedule': 5,
        'args': (5,),
    },
}

# FIXME
app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'Cron.tasks.hello',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
}
