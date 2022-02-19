from django.db import models


class Image(models.Model):
    """Model which contains cloth image"""
    image = models.ImageField()

    @property
    def image_url(self):
        return self.image.url


