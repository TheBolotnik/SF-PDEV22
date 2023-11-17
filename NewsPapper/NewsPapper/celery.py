import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPapper.settings')

app = Celery('NewsPapper')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

'''celery -A NewsPapper worker -l INFO --pool=solo'''


app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'action',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        'args': (agrs),
    },
}

app.conf.beat_schedule = {
    'weekly_news': {
        'task': 'news.tasks.tasks.weekly_news',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
}