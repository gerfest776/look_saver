from django.db.models import Prefetch
from django_filters import rest_framework
from django_filters.rest_framework import filters

from look_collector.models import Outfit, OutfitItem


class OutfitBrand(filters.CharFilter):
    def filter(self, qs, value):
        if value is not None:
            return qs.prefetch_related(
                Prefetch("look_id", queryset=OutfitItem.objects.filter(brand=value))
            )
        else:
            return qs


class OutfitItemFilter(rest_framework.FilterSet):
    brand = OutfitBrand()

    class Meta:
        model = Outfit
        fields = ["brand"]
