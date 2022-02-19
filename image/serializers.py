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
        image_processing.delay(validated_data['image'])




    def to_representation(self, instance):
        representation = super(ImageSerializer, self).to_representation(instance)
        return representation
