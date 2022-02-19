from io import BytesIO

from PIL import Image as Im
from django.core.files.uploadhandler import InMemoryUploadedFile
from look_saver.celery import celery_app


@celery_app.task(bind=True, name='Image processing')
def image_processing(instance):
    pic_name = instance.image.name
    pic_object = Im.open(instance.image)

    thumbnail = BytesIO
    pic_object.convert('RGBA').save(thumbnail, optimize=True,
                                      quality=50, format='PNG')
    thumbnail.seek(0)

    instance.image = InMemoryUploadedFile(thumbnail, 'ImageField', "%s.png" % pic_name.split('.')[0],
                                          'image/jpeg', thumbnail.tell(), None)
    instance.save()


