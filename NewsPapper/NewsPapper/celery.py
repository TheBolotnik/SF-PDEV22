import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPapper.settings')

app = Celery('NewsPapper')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

'''celery -A NewsPapper worker -l INFO --pool=solo'''