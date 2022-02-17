from rest_framework.routers import DefaultRouter

from look_collector import views

router = DefaultRouter(trailing_slash=False)
router.register(r'looks', views.LookView)


urlpatterns = [
]

urlpatterns += router.urls
