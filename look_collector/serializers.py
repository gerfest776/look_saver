from rest_framework import serializers

from look_collector.models import Look, LookItem


class LookItemSerialize(serializers.ModelSerializer):
    class Meta:
        model = LookItem
        fields = '__all__'


class LookImportSerializer(serializers.ModelSerializer):
    look = LookItemSerialize(many=True, write_only=True)

    class Meta:
        model = Look
        fields = '__all__'
