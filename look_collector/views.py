from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from look_collector.models import Outfit
from look_collector.serializers import LookImportSerializer


class LookView(CreateModelMixin, GenericViewSet):
    queryset = Outfit.objects.all()
    serializer_class = LookImportSerializer

    # def get_serializer_class(self):
    #     serializer = self.serializer_class(data=self.request.user)
    #     return serializer(data=self.request.user)




