from rest_framework import serializers

from image.tasks import size_reduce
from look_collector.models import Image


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True)
    image_url = serializers.CharField(read_only=True)

    class Meta:
        model = Image
        fields = "__all__"

    def create(self, validated_data):
        image = Image.objects.create(**validated_data)
        size_reduce.delay(image.id)
        return image.id

    def to_representation(self, instance):
        representation = {"id": instance}
        return representation
