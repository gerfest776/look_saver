import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "look_saver.settings")

celery_app = Celery("look_saver")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()


@celery_app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')