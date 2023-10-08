from django.db import models
from django.contrib.auth.models import User, Group
from django.urls import reverse


type = [
    ('ARTICLE', 'Статья'),
    ('NEWS', 'Новость')
]

oauth_user = Group.objects.get(name='authors')


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Содержание')
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,  verbose_name='Категория')
    auth = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Автор', blank=True, default='admin')

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


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name_plural = 'Категории'


class NewsCategory(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=50),
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('authors', kwargs={'user_auth_id': self.pk})


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