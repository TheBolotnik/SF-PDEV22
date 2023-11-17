import smtplib
from NewsPapper.news.models import *
from NewsPapper.news.signals import notify_news_subscriber, send_notifications
from django.http import HttpResponse
from django.views import View
from celery import Celery, shared_task
from celery.schedules import crontab

@shared_task
def weekly_news():
    send_news = notify_news_subscriber
    return send_news


@shared_task
def hello():
    time.sleep(2)
    print('Hello World!')


@shared_task
def printer(N):
    for i in range(N):
        time.sleep(1)
        print(i+1)


class MyTask(View):
    def get(self, request):
        printer.delay(10)
        hello.delay()
        return HttpResponse('Hello world!')