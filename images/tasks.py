from io import BytesIO

from PIL import Image as Im
from django.core.files.uploadhandler import InMemoryUploadedFile
from look_saver.celery import celery_app


@celery_app.task(bind=True, name='Image load')
def image_load(instance):
    image_name = instance.image.name
    image_object = Im.open(instance.image)

    thumbnail = BytesIO
    instance.image = image_object.convert('RGBA').save(thumbnail, optimize=True,
                                      quality=50, format='PNG')
    thumbnail.seek(0)

    instance.image = InMemoryUploadedFile(thumbnail, 'ImageField', "%s.png" % image_name.split('.')[0],
                                          'images/jpeg', thumbnail.tell(), None)
    instance.save()


