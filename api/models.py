import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Shoes(models.Model):
    shoes_id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=30)
    size = models.CharField(max_length=5)
    color = models.CharField(max_length=15)
    link = models.CharField(max_length=150)
    image = models.ImageField(upload_to='shoes_media')

    class Meta:
        db_table = 'shoes'


class Pants(models.Model):
    pants_id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=30)
    size = models.CharField(max_length=5)
    color = models.CharField(max_length=15)
    link = models.CharField(max_length=150)
    image = models.ImageField(upload_to='pants_media')

    class Meta:
        db_table = 'pants'


class Top(models.Model):
    top_id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=30)
    size = models.CharField(max_length=5)
    color = models.CharField(max_length=15)
    link = models.CharField(max_length=150)
    image = models.ImageField(upload_to='top_media')

    class Meta:
        db_table = 'top'


class Accessory(models.Model):
    accessory_id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=30)
    size = models.CharField(max_length=5)
    color = models.CharField(max_length=15)
    link = models.CharField(max_length=150)
    image = models.ImageField(upload_to='accessory_media')

    class Meta:
        db_table = 'accessory'


class Look(models.Model):
    look_id = models.AutoField(primary_key=True)
    accessory_id = models.ForeignKey(Accessory, null=True, related_name='look', on_delete=models.SET_NULL)
    top_id = models.ForeignKey(Top, null=True, related_name='look', on_delete=models.SET_NULL)
    pants_id = models.ForeignKey(Pants, null=True, related_name='look', on_delete=models.SET_NULL)
    shoes_id = models.ForeignKey(Shoes, null=True, related_name='look', on_delete=models.SET_NULL)
    # user_id = models.ForeignKey(User, related_name='look', on_delete=models.CASCADE)

    class Meta:
        db_table = 'look'
