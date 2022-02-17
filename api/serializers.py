from rest_framework import serializers

from api.models import Accessory
from api.models import Pants
from api.models import Shoes
from api.models import Top


class PantsSerializer(serializers.ModelSerializer):
    link = serializers.URLField(max_length=200)
    image = serializers.ImageField(allow_empty_file=False)

    class Meta:
        model = Pants
        fields = "__all__"

    def create(self, validated_data):
        return Pants.objects.create(**validated_data)


class ShoesSerializer(serializers.ModelSerializer):
    link = serializers.URLField(max_length=200)
    image = serializers.ImageField(allow_empty_file=False)

    class Meta:
        model = Shoes
        fields = "__all__"


class TopSerializer(serializers.ModelSerializer):
    link = serializers.URLField(max_length=200)
    image = serializers.ImageField(allow_empty_file=False)

    class Meta:
        model = Top
        fields = "__all__"


class AccessorySerializer(serializers.ModelSerializer):
    link = serializers.URLField(max_length=200)
    image = serializers.ImageField(allow_empty_file=False)

    class Meta:
        model = Accessory
        fields = "__all__"


class LookSerializer(serializers.ModelSerializer):
    pass
