from django.urls import path
from rest_framework.routers import DefaultRouter

from look_collector import views
from look_collector.views import LookView

villager_router = DefaultRouter(trailing_slash=False)
villager_router.register("outfit", views.LookView)


urlpatterns = [
]


urlpatterns += villager_router.urls
