from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from django.template.loader import render_to_string

from Buulitin_board import settings
from .models import *


def send_reply(preview, pk, title, subscribers):
    html_context = render_to_string(
        'reply.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/post/{pk}',
        }

    )
    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers
    )
    msg.attach_alternative(html_context, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=Reply)
def notify_reply(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        pass


