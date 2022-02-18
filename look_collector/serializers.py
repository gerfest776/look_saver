from django.db import transaction
from rest_framework import serializers

from look_collector.models import Outfit, OutfitItem


class LookItemSerialize(serializers.ModelSerializer):
    class Meta:
        model = OutfitItem
        exclude = ['look_id']


class LookImportSerializer(serializers.ModelSerializer):
    outfit = LookItemSerialize(many=True, write_only=True)

    class Meta:
        model = Outfit
        fields = ['outfit']

    def create(self, validated_data):
        current_outfit = Outfit.objects.create(owner_id=self.context['request'].user.id)

        result = OutfitItem.objects.bulk_create(
            [OutfitItem(**outfit_detail) for outfit_detail in validated_data['outfit']]
        )

        current_outfit.look.set(cloth.id for cloth in result)
        return current_outfit

    def to_representation(self, instance):
        representation = super(LookImportSerializer, self).to_representation(instance)
        representation['outfit'] = {"outfit_id": instance.id}
        return representation


class UpOutfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutfitItem
        exclude = ['look_id']


class OutfitSerializer(serializers.ModelSerializer):
    # look_id = serializers.PrimaryKeyRelatedField()
    class Meta:
        model = Outfit
        fields = ['id']


class PartialSerializer(serializers.ModelSerializer):

    class Meta:
        model = OutfitItem
        fields = [
            'type',
            'brand',
            'price',
            'size',
            'color',
            'link',
            'image'
        ]

        extra_kwargs = {
            "type": {"required": False},
            "brand": {"required": False},
            "price": {"required": False},
            "size": {"required": False},
            "color": {"required": False},
            "link": {"required": False},
            "image": {"required": False},
        }

    def update(self, obj, validated_data):
        obj = obj.look.filter(id=self.context['view'].kwargs['cloth_id']).first()
        for attr, value in validated_data.items():
            setattr(obj, attr, value)
        obj.save()
        return obj


class RetrieveSerializer(serializers.ModelSerializer):

    class Meta:

