import json

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import serializers

from image.tasks import image_processing
from look_collector.models import Image


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True)
    image_url = serializers.CharField(read_only=True)

    class Meta:
        model = Image
        fields = '__all__'

    def create(self, validated_data):
        file = Image.objects.create(**validated_data)
        instance = image_processing.delay(file.id)
        return file

    def to_representation(self, instance):
        representation = super(ImageSerializer, self).to_representation(instance)
        return representation
