from django.db import models

# Create your models here.


# class ReplyFilter(models.Manager):
#     reply = models.ForeignKey(Reply, on_delete=models.CASCADE, blank=True, related_name='reply_filter')
#
#     def get_queryset(self):
#         #return super().get_queryset().filter(status=False)
#         return super().get_queryset().all()