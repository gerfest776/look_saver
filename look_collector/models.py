import enum
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from image.models import Image


class User(AbstractUser):
    """Basic  user auth model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        db_table = 'user'


class OutfitItem(models.Model):
    """Model with look_item"""
    class Items(enum.Enum):
        pants = 'Штаны'
        top = 'Верхняя одежда'
        shoes = 'Обувь'
        accessory = 'Аксессуары'

        @classmethod
        def to_choices(cls):
            return tuple((i.name, i.value) for i in cls)

    type = models.CharField(max_length=64, choices=Items.to_choices())
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=5)
    color = models.CharField(max_length=15)
    link = models.CharField(max_length=150)
    image_id = models.ForeignKey(Image, null=True, on_delete=models.SET_NULL, related_name='look_item')

    class Meta:
        db_table = 'outfit_item'


class Outfit(models.Model):
    """Model with look"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    look_id = models.ManyToManyField(OutfitItem, null=True, related_name='outfit')

    class Meta:
        db_table = "outfit"

