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
    lookup_field = "id"
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = OutfitItemFilter

    def get_queryset(self):
        pass
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
    def outfits_partial(self, request, id, cloth_id):
        return self.partial_update(request)

    @action(methods=["get"], detail=True, url_path="my_outfits/")
    def outfits_retrieve(self, request, id):
        return self.retrieve(request)

    @action(methods=["delete"], detail=True, url_path="del_outfits")
    def all_outfit_destroy(self, request, id):
        obj = self.get_object()
        instance = self.get_object().look_id.all()
        self.perform_destroy(instance)
        self.perform_destroy(obj)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        methods=["delete"], detail=True, url_path="del_outfits/(?P<cloth_id>[^/.]+)"
    )
    def outfits_destroy(self, request, id, cloth_id):
        instance = self.get_object().look_id.filter(id=cloth_id).first()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
