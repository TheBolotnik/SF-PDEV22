from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#from users.models import ReplyFilter


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(verbose_name='Описание')
    images = models.ImageField(upload_to='images/%Y/%m/%d/', default=None, blank=True, null=True, verbose_name='Изображения')
    date = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор')

    def __str__(self):
        return self.title

    def preview(self):
        preview = f'{self.content[:50]}...'
        return preview

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reply_post')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор отклика")
    text = models.TextField(verbose_name="Текст отклика")
    datetime = models.DateTimeField(auto_now_add=True)
    reply_status = models.BooleanField(verbose_name="Опубликовано", default=False)

    def __str__(self):
        return self.text

    def priview(self):
        preview = f'{self.text[:124]}...'
        return preview


class UploadFiles(models.Model):
    file = models.FileField(upload_to='uploads_model')