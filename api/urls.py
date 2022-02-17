from django.urls import path

from rest_framework.routers import DefaultRouter

from api import views
from api.views import LookView

router = DefaultRouter(trailing_slash=False)
router.register('looks', views.LookView)

urlpatterns = [

]

urlpatterns += router.urls