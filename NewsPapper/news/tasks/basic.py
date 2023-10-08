from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def get_subscribers(category):
    user_email = []
    for user in category.subscribers.all():
        user_email.append(user_email)
    return user_email

def new_post_subscribtion(instatce):
    template = 'news/new_post'

    for category in instatce.category.all():
        email_subject = f'Новый пост в категории "{category}"'
        user_email = get_subscribers(category)

        html = render_to_string(
            template_name=template,
            context={
                'category': category,
                'post': instatce
            }
        )

        msg = EmailMultiAlternatives(
            subject=email_subject,
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=user_email
        )
        msg.attach_alternative(html, 'text/html')
        msg.send()