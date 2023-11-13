import smtplib

from celery import Celery, shared_task
from email.message import EmailMessage
from NewsPapper.NewsPapper.settings import SMTP_USER, SMTP_PASSWORD
import time


SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465


# def get_email_template(username: str):
#     email = EmailMessage()
#     email['Subject'] = 'Новостной портал'
#     email['From'] = SMTP_USER
#     email['To'] = SMTP_USER
#
#     email.set_content(
#         '<div>'
#         f'<h1>Здравствуйте {username}, вы пропустили следующие <a href="/home">новости:</a></h1>'
#         '</div>',
#         subtype='html'
#     )
#     return email
#
#
# def send_email_news(username: str):
#     email = get_email_template(username)
#     with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
#         server.login(SMTP_USER, SMTP_PASSWORD)
#         server.send_message(email)


@shared_task
def hello():
    time.sleep(10)
    print('Hello World!')


def printer(N):
    for i in range(N):
        time.sleep(1)
        print(i+1)

# def get(self, request):
#     printer.delay(10)
#     hello.delay()
#     from django.http import HttpResponse
#     return HttpResponse('Hello!')