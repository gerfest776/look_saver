from django.urls import path

from rest_framework.routers import DefaultRouter

from image import views

router = DefaultRouter(trailing_slash=False)
router.register("image", views.ImageView)


urlpatterns = [
]

urlpatterns += router.urls
