from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from look_collector.models import Outfit, OutfitItem, User
from look_collector.serializers import LookImportSerializer, OutfitSerializer


class LookView(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = Outfit.objects.all()
    serializer_class = LookImportSerializer
    # lookup_field = 'id'

    def get_queryset(self):
        if self.action == 'my_outfits':
            objs = Outfit.objects.select_related('owner').\
                filter(owner_id=self.kwargs['id'])
            return objs
        else:
            return self.queryset

    def get_serializer_class(self):
        if self.action == 'my_outfits':
            return OutfitSerializer
        else:
            return self.serializer_class

    @action(methods=['get'], detail=False, url_path='my_outfits/(?P<id>[^/.]+)')
    def my_outfits(self, request, id):
        return self.list(request)
