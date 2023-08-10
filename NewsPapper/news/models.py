from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser
from django.urls import reverse


#import views


type = [
    ('ARTICLE', 'Статья'),
    ('NEWS', 'Новость')
]

class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    #user_cat = models.ManyToManyField('Category', through='Subscribers')


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name_plural = 'Категории'


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Содержание')
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,  verbose_name='Категория')
    auth = models.ForeignKey('Author', null=True, blank=True, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'News'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class Author(models.Model):
    name = models.CharField(max_length=255),
    user = models.ForeignKey('User', on_delete=models.CASCADE)


class NewsCategory(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    news_com = models.ForeignKey(News, on_delete=models.CASCADE)
    news_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    com_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)


    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()