from rest_framework import serializers

from look_collector.models import Outfit, OutfitItems


class LookItemSerialize(serializers.ModelSerializer):
    class Meta:
        model = OutfitItems
        exclude = ['look_id']


class LookImportSerializer(serializers.ModelSerializer):
    look = LookItemSerialize(many=True)

    class Meta:
        model = Outfit
        fields = ['look']

    def to_representation(self, instance):
