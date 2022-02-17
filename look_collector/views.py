from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from look_collector.models import Look
from look_collector.serializers import LookImportSerializer


class LookView(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Look.objects.all()
    serializer_class = LookImportSerializer

    @action(methods=['get'], detail=True)
    def check(self):
        pass


