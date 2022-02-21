from idlelib.pyshell import HOST, PORT

from django.db import models


class Image(models.Model):
    """Model which contains cloth image"""

    image = models.ImageField(null=True)

    @property
    def image_url(self):
        return f'{HOST}:8000{self.image.url}'
