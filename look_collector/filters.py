import django_filters
from django.db.models import Prefetch
from django_filters import rest_framework, CharFilter, Filter

from look_collector.models import OutfitItem, Outfit


class OutfitItemFilter(rest_framework.FilterSet):
    """
    Filter for OutfitItem

    QueryParams:
            order_by - field which sorts by price(order_by = <UUID>)
            brand - field which sorts by brand(brand = <UUID>)
    """

    # order_by = django_filters.OrderingFilter(fields=['price'])

    brand = django_filters.CharFilter(field_name='brand', method='brand_filter')

    class Meta:
        model = Outfit
        fields = ['id','brand']

    # def brand_filter(self, queryset, name,  value):
    #     list = []
    #     for query in queryset:
    #         dict = {f"outfit_id {query.id}" : []}
    #         for outfititem in query.look_id.all():
    #             if outfititem.brand == value:
    #                 dict[f"outfit_id {query.id}"].append(outfititem)
    #         list.append(dict)
    #     queryset = list_to_queryset(list)
    #     return Outfit.objects.filter()
