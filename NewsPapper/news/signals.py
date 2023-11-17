from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import *
#from NewsPapper.news.tasks.tasks import new_post_subscribtion


def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
        'news_created.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(post_save, sender=Category)
def notify_news_subscriber(sender, instance, **kwargs):
    if kwargs['action'] == 'news_add':
        categories = instance.name.all()
        subscribers: list[str] = []

        for cat in categories:
            subscribers += cat.subscribers.all()

        subscribers = [s.email for s in subscribers]

        send_notifications(instance.preview(). instance.pk, instance.title, subscribers)