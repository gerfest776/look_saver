import io

from django.core.files.uploadhandler import InMemoryUploadedFile
from PIL import Image as Im

from image.models import Image
from look_saver.celery import celery_app


@celery_app.task(bind=True, name="Size reduce")
def size_reduce(first, check):
    instance = Image.objects.get(id=check)
    pic_name = instance.image.name
    pic_object = Im.open(instance.image)

    thumbnail = io.BytesIO()
    pic_object.convert("RGBA").save(thumbnail, optimize=True, quality=50, format="PNG")
    thumbnail.seek(0)

    image = InMemoryUploadedFile(
        thumbnail,
        "ImageField",
        "%s.png" % pic_name.split(".")[0],
        "image/jpeg",
        thumbnail.tell(),
        None,
    )
    instance.image = image
    instance.save()
