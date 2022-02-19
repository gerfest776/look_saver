from django.urls import path

from rest_framework.routers import DefaultRouter

from images import views

router = DefaultRouter(trailing_slash=False)
router.register("images", views.ImageView)


urlpatterns = [
]

urlpatterns += router.urls
