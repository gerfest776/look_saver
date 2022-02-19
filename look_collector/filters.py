import django_filters
from django_filters import rest_framework, CharFilter

from look_collector.models import OutfitItem


class OutfitItemFilter(rest_framework.FilterSet):
    """
    Filter for OutfitItem

    QueryParams:
            order_by - field which sorts by price(order_by = <UUID>)
            price - field which sorts by price(price = <UUID>)
            brand - field which sorts by brand(brand = <UUID>)
    """

    order_by = django_filters.OrderingFilter(fields=['price'])

    class Meta:
        model = OutfitItem
        fields = ['price', 'brand']
