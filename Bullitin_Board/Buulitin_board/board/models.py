from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    #author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title

    def preview(self):
        preview = f'{self.content[:50]}...'
        return preview

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

class Category(models.Model):
    name = models.CharField(max_length=50)
    #subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


class Profile(models.Model):
    pass


class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Пользователь {User} прокомментировал: {self.text[:50]}...'