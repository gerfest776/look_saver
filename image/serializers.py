from rest_framework import serializers

from look_collector.models import Image


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True)
    image_url = serializers.CharField(read_only=True)

    class Meta:
        model = Image
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(ImageSerializer, self).to_representation(instance)
        return representation
