import base64
import io
from django.db import models



# Create your models here.


class Users(models.Model):
    email = models.EmailField(max_length=50)
    full_name = models.CharField(max_length=255)
    phone = models.IntegerField()

    def __str__(self):
        return self.full_name


class Coord(models.Model):
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=10, decimal_places=8)
    height = models.IntegerField()

    def __str__(self):
        return str(self.height)


class Level(models.Model):

    LEVEL_1 = '1A'
    LEVEL_2 = '1B'
    LEVEL_3 = '2A'
    LEVEL_4 = '2B'
    LEVEL_5 = '3A'
    LEVEL_6 = '3B'
    LEVEL_CHOICES = (
        ('1A', '1A'),
        ('1B', '1B'),
        ('2A', '2A'),
        ('2B', '2B'),
        ('3A', '3A'),
        ('3B', '3B')
    )

    winter = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LEVEL_1)
    summer = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LEVEL_1)
    autumn = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LEVEL_1)
    spring = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LEVEL_1)

    def __str__(self):
        return f' winter: {self.winter}, summer: {self.summer}, autumn: {self.autumn}, spring: {self.spring}'


class Images(models.Model):
    data = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    pereval_id = models.ForeignKey('PerevalAdd', on_delete=models.CASCADE, related_name='image')

    def __str__(self):
        return f'title: {self.title}'


class PerevalAdd(models.Model):
    new = 'new'
    pending = 'pending'
    accepted = 'accepted'
    rejected = 'rejected'
    STATUS = [
        (new, 'new'),
        (pending, 'is being done'),
        (accepted, 'successfully moderated'),
        (rejected, 'was moderated but was not accepted')
    ]

    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255, null=True, blank=True)
    connect = models.CharField(max_length=255)
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS, default=new)

    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

    coords_id = models.OneToOneField(Coord, on_delete=models.CASCADE)

    level_diff = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk}:  {self.beauty_title}'
