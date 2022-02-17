from django.urls import path
from rest_framework.routers import DefaultRouter

from look_collector import views
from look_collector.views import LookView

router = DefaultRouter(trailing_slash=False)
router.register("outfit", views.LookView)


urlpatterns = [
]


urlpatterns += router.urls
