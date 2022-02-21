from decimal import Decimal

import django_filters
from django.db.models import Prefetch
from django_filters import CharFilter, Filter, rest_framework
from django_filters.rest_framework import filters

from look_collector.models import Outfit, OutfitItem


class OutfitBrand(filters.CharFilter):
    def filter(self, qs, value):
        if value is not None:
            return qs.prefetch_related(
                Prefetch(
                    'look_id',
                    queryset=OutfitItem.objects.filter(brand=value)
                )
            )
        else:
            return qs


class OutfitItemFilter(rest_framework.FilterSet):
    """
    Filter for OutfitItem

    QueryParams:
            brand - field which sorts by brand(brand = <UUID>)
            price - field which sorts by price(price = <UUID>)
    """
    brand = OutfitBrand()

    class Meta:
        model = Outfit
        fields = ["brand"]
