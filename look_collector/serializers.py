from django.db import transaction
from rest_framework import serializers

from look_collector.models import Outfit, OutfitItem


class LookItemSerialize(serializers.ModelSerializer):
    class Meta:
        model = OutfitItem
        exclude = ['look_id']


class LookImportSerializer(serializers.ModelSerializer):
    look = LookItemSerialize(many=True)

    class Meta:
        model = Outfit
        fields = ['look']

    def create(self, validated_data):
        all_outfits = []
        with transaction.atomic():
            current_outfit = Outfit.objects.create(owner_id=self.context['request'].user.id)

            for outfit_detail in validated_data['look']:
                all_outfits.append(OutfitItem(**outfit_detail))
            OutfitItem.objects.bulk_create(all_outfits)
            current_outfit.look.set(all_outfits)

            return current_outfit


    def to_representation(self, instance):
        representation = super(LookImportSerializer, self).to_representation(instance)
        representation['look'] = LookImportSerializer(instance.look.all(), many=True).data
        return representation

