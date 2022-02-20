import base64
import io
from base64 import b64decode
from io import BytesIO

from django.core.files.uploadhandler import InMemoryUploadedFile
from PIL import Image as Im

from image.models import Image
from look_saver.celery import celery_app


@celery_app.task(bind=True, name="Image processing")
def image_processing(instance, inmemobj, *args, **kwargs):
    instance = Image.objects.get(id=instance)
    pic_name = instance.image.name
    pic_object = Im.open(instance.image)

    thumbnail = BytesIO()
    pic_object.convert("RGBA").save(thumbnail, optimize=True, quality=50, format="PNG")
    thumbnail.seek(0)

    instance.image = InMemoryUploadedFile(
        thumbnail,
        "ImageField",
        "%s.png" % pic_name.split(".")[0],
        "image/jpeg",
        thumbnail.tell(),
        None,
    )
    instance.save()
