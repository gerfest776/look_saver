from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from api.models import Look
from api.serializers import LookSerializer


class LookView(CreateModelMixin, GenericViewSet):
    queryset = Look.objects.all()
    serializer_class = LookSerializer
