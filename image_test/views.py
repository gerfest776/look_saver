from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin
from rest_framework.parsers import MultiPartParser

from image_test.serializers import ImageSerializer
from look_collector.models import Image
# Create your views here.
from rest_framework.viewsets import GenericViewSet


class ImageView(CreateModelMixin, GenericViewSet):
    queryset = Image.objects.all()
    Serializer = ImageSerializer
    parser_classes = (MultiPartParser,)
