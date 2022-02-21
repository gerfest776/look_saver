from collections.abc import KeysView

from django.db.models import Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from look_collector.filters import OutfitItemFilter
from look_collector.models import Outfit, OutfitItem, User
from look_collector.pagination import Pagination
from look_collector.serializers import (
    LookImportSerializer,
    OutfitSerializer,
    PartialSerializer,
    RetrieveSerializer,
)


class LookView(
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    queryset = Outfit.objects.all()
    serializer_class = LookImportSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend]
    search_fields = ['brand', 'price', 'type']

    def get_queryset(self):
        if self.action == "my_outfits":
            qs = Outfit.objects.filter(owner_id=self.request.user.id)
            return qs
        else:
            return self.queryset

    def get_serializer_class(self):
        if self.action == "my_outfits":
            return OutfitSerializer
        elif self.action == "outfits_partial":
            return PartialSerializer
        elif self.action == "outfits_retrieve":
            return RetrieveSerializer
        else:
            return self.serializer_class

    @action(methods=["get"], detail=False, url_path="my_outfits")
    def my_outfits(self, request):
        return self.list(request)

    @action(methods=["patch"], detail=True, url_path="my_outfits/(?P<cloth_id>[^/.]+)")
    def outfits_partial(self, request, pk, cloth_id):
        return self.partial_update(request)

    @action(methods=["get"], detail=True, url_path="my_outfits/")
    def outfits_retrieve(self, request, pk):
        return self.retrieve(request)

    def destroy(self, request, *args, **kwargs):
        query_params = self.request.query_params.dict()
        obj = self.get_object()
        if not query_params:
            obj.look_id.clear()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            for param in query_params.keys():
                if param in [item for item in OutfitItem.Items.to_choices()]:
                    param = int(query_params[param])
                    obj.look_id.remove(param)
            return Response(status=status.HTTP_204_NO_CONTENT)
