from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
#from NewsPapper.news.tasks.tasks import new_post_subscribtion


@receiver(post_save, sender=Category)
def notify_news_subscriber(sender, instance, **kwargs):
    # if kwargs['action'] == 'news.add':
    #     new_post_subscribtion(instance)
    pass