from django.db import models
#import views

'''director = 'DI'
admin = 'AD'
cook = 'CO'
cashier = 'CA'
cleaner = 'CL'

POSITION = [
    (director, 'Директор'),
    (admin, 'Администратор'),
    (cook, 'Повар'),
    (cashier, 'Кассир'),
    (cleaner, 'Уборщик')
]


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default = 0.0)
    composition = models.TextField(default= 'Состав не указан')


class Stuff(models.Model):
    stuff_id = models.AutoField
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=2, choices= POSITION, default=cashier)
    labor_contract = models.IntegerField(default=0)

    def get_last_name(self):
        return self.full_name.split()[0]


class Order(models.Model):
    time_in = models.DateTimeField(auto_now_add = True)
    time_out = models.DateTimeField(null = True)
    cost = models.FloatField(default = 0.0)
    pickup = models.BooleanField(default = False)
    complete = models.BooleanField(default= False)
    stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE)

    products = models.ManyToManyField(Product, through= 'ProductOrder')

    def finish_order(self):
        self.time_out = datetime.now()
        self.complete = True
        self.save()

    def get_durations(self):
        if self.complete:
            return (self.time_out - self.time_in).total_seconds() // 60
        else:
            return (datetime.now(timezone.utc) - self.time_in).total_seconds() // 60


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    _amount = models.IntegerField(default=1, db_column= 'amount')

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = int(value) if value >=0 else 0
        self.save()


    def product_sum(self):
        product_price = self.product.price
        return product_price * self.amount'''
'''class News(models.Model):
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

from django.contrib.auth.models import User

type = [
    ('ARTICLE', 'Статья'),
    ('NEWS', 'Новость')
]

class News(models.Model):
    pass

class Author(models.Model):
    name = models.CharField(max_length=255),
    user = models.OneToOneField('User', on_delete=models.CASCADE),

class Category(models.Model):
        uniq = True
class Post(models.Model):
    title = models.CharField(max_length=255),
    content = models.TextField,
    authors = models.ForeignKey(Author, on_delete=models.CASCADE),
    post_type = models.CharField(max_length=10, choices=type),
    date = models.DateTimeField(auto_now_add=True),
    post_cat = models.ManyToManyField(Category, through='PostCategory'),
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE),
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post_com = models.ForeignKey(Post, on_delete=models.CASCADE),
    post_user = models.ForeignKey(User, on_delete=models.CASCADE),
    comment = models.TextField,
    com_date = models.DateTimeField(auto_now_add=True),
    rating = models.IntegerField(default=0)


    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()