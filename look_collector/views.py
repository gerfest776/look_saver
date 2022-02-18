from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from look_collector.models import Outfit, OutfitItem, User
from look_collector.serializers import LookImportSerializer, OutfitSerializer, PartialSerializer, RetrieveSerializer


class LookView(CreateModelMixin,
               ListModelMixin,
               RetrieveModelMixin,
               UpdateModelMixin,
               DestroyModelMixin,
               GenericViewSet):
    queryset = Outfit.objects.all()
    serializer_class = LookImportSerializer
    lookup_field = 'id'

    def get_queryset(self):
        pass
        if self.action == 'my_outfits':
            objs = Outfit.objects.filter(owner_id = self.kwargs['owner_id'])
            return objs
        else:
            return self.queryset

    def get_serializer_class(self):
        if self.action == 'my_outfits':
            return OutfitSerializer
        elif self.action == 'outfits_partial':
            return PartialSerializer
        elif self.action == 'outfits_retrieve':
            return RetrieveSerializer
        else:
            return self.serializer_class

    @action(methods=['get'], detail=False, url_path='my_outfits/(?P<owner_id>[^/.]+)')
    def my_outfits(self, request, owner_id):
        return self.list(request)

    @action(methods=['patch'], detail=True, url_path='my_outfits/(?P<cloth_id>[^/.]+)')
    def outfits_partial(self, request, id, cloth_id):
        return self.partial_update(request)

    @action(methods=['get'], detail=True, url_path='my_outfits/')
    def outfits_retrieve(self, request, id):
        return self.retrieve(request)

    @action(methods=['destroy'], detail=True, url_path='del_outfits')
    def outfits_destroy(self, request, id):
        return self.destroy(request)

