from rest_framework import serializers

from look_collector.models import Outfit, OutfitItem


class LookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutfitItem
        fields = "__all__"


class LookImportSerializer(serializers.ModelSerializer):
    outfit = LookItemSerializer(many=True, write_only=True)

    class Meta:
        model = Outfit
        fields = ["outfit"]

    def create(self, validated_data):
        """
        create outfit obj with owner_id, after bulk_create outfititem
        outfit obj set relatvies
        """
        current_outfit = Outfit.objects.create(owner_id=self.context["request"].user.id)
        result = OutfitItem.objects.bulk_create(
            [OutfitItem(**outfit_detail) for outfit_detail in validated_data["outfit"]]
        )
        current_outfit.look_id.set(cloth.id for cloth in result)
        return current_outfit

    def to_representation(self, instance):
        representation = super(LookImportSerializer, self).to_representation(instance)
        representation["outfit"] = {"outfit_id": instance.id}
        return representation


class OutfitSerializer(serializers.ModelSerializer):
    outfit = LookItemSerializer(source="look_id", many=True, read_only=True)

    class Meta:
        model = Outfit
        fields = ["outfit"]
        # depth = 1


class PartialSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutfitItem
        fields = ["type", "brand", "price", "size", "color", "link", "image_id"]

        extra_kwargs = {
            "type": {"required": False},
            "brand": {"required": False},
            "price": {"required": False},
            "size": {"required": False},
            "color": {"required": False},
            "link": {"required": False},
            "image_id": {"required": False},
        }

    def update(self, obj, validated_data):
        obj = obj.look_id.filter(id=self.context["view"].kwargs["cloth_id"]).first()
        for attr, value in validated_data.items():
            setattr(obj, attr, value)
        obj.save()
        return obj


class RetrieveSerializer(serializers.ModelSerializer):
    look_id = LookItemSerializer(many=True, read_only=True)
    outfit = look_id

    class Meta:
        model = Outfit
        fields = ["id", "look_id", "outfit"]
