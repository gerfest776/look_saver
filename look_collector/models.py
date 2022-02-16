from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)


class Shoes(models.Model):
    shoes_id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=30)
    size = models.CharField(max_length=5)
    color = models.CharField(max_length=15)
    link = models.CharField(max_length=150)
    image = models.ImageField(upload_to='shoes_media')


class Pants(models.Model):
    pants_id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=30)
    size = models.CharField(max_length=5)
    color = models.CharField(max_length=15)
    link = models.CharField(max_length=150)
    image = models.ImageField(upload_to='pants_media')


class Top(models.Model):
    top_id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=30)
    size = models.CharField(max_length=5)
    color = models.CharField(max_length=15)
    link = models.CharField(max_length=150)
    image = models.ImageField(upload_to='top_media')


class Accessory(models.Model):
    accessory_id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=30)
    size = models.CharField(max_length=5)
    color = models.CharField(max_length=15)
    link = models.CharField(max_length=150)
    image = models.ImageField(upload_to='accessory_media')



