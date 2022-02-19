from django.db import models


class Image(models.Model):
    """Model which contains cloth image"""
    image = models.ImageField(upload_to='media')

