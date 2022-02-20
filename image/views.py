from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin
from rest_framework.parsers import MultiPartParser

# Create your views here.
from rest_framework.viewsets import GenericViewSet

from image.serializers import ImageSerializer
from look_collector.models import Image


class ImageView(CreateModelMixin, GenericViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser,)
