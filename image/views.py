from django.shortcuts import render

from image.serializers import ImageSerializer
from look_collector.models import Image
# Create your views here.
from rest_framework.viewsets import GenericViewSet


class ImageView(GenericViewSet):
    queryset = Image.objects.all()
    Serializer = ImageSerializer