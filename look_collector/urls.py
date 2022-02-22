from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from look_collector import views
from look_collector.views import LookView

router = DefaultRouter(trailing_slash=False)
router.register("outfit", views.LookView)


urlpatterns = [
    path("outfit", LookView.as_view({"post": "create"})),
    path("outfit/<int:pk>", LookView.as_view({"delete": "destroy"})),
    path("token", TokenObtainPairView.as_view(), name="token_obta   in_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]


urlpatterns += router.urls
