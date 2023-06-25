from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.urls import reverse
#import views

'''
class News(models.Model):
    date = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    
         def preview(self):
            preview_len = 124
            if preview_len >= 124:
                return self.content[:preview_len] + '...'
            else:
                return self.content
    
'''


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

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name_plural = 'Categories'

class News(models.Model):
    date = models.CharField(max_length=20)
    title = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=20, blank=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'News'



class Author(models.Model):
    name = models.CharField(max_length=255),
    user = models.ForeignKey('User', on_delete=models.CASCADE)



class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=10, choices=type)
    post_date = models.DateTimeField(auto_now_add=True)
    post_cat = models.ManyToManyField(Category, through='PostCategory')
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post_com = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    com_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)


    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()