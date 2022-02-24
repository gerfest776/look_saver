from django.db import models

from look_saver.settings import HOST


class Image(models.Model):
    """Model which contains cloth image"""

    image = models.ImageField(null=True)

    @property
    def image_url(self):
        return f"{HOST}{self.image.url}"
