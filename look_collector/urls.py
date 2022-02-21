from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from look_collector import views
from look_collector.views import LookView

router = DefaultRouter(trailing_slash=False)
router.register("outfit", views.LookView)
print(2)


urlpatterns = [
    path("outfit", LookView.as_view({"post": "create"})),
    # path("outfit/<pk>", LookView.as_view({"delete": "destroy"})),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]


urlpatterns += router.urls
