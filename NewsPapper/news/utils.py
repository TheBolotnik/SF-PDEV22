from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from NewsPapper import settings
#from django.conf import settings
from .models import Category

menu = [
    {'title': 'Главная страница', 'url_name': 'home' },
    {'title': 'Новости', 'url_name': 'news'},
    {'title': 'Добавить новость', 'url_name': 'add_news'},
    {'title': 'Поиск', 'url_name': 'search'},
]


class DataMixin():
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context


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

    msg.attach_alternative()