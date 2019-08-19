from django_filters import rest_framework as filters
from django_filters import DateTimeFilter, TimeRangeFilter, IsoDateTimeFilter, DateRangeFilter, BaseInFilter, CharFilter

from .models import Order



class OrderStatusInFilter(BaseInFilter, CharFilter):
    pass

class OrderFilter(filters.FilterSet):
    start_time = IsoDateTimeFilter(field_name='pickup_time',lookup_expr=('gt'),)
    end_time = IsoDateTimeFilter(field_name='pickup_time',lookup_expr=('lt'))
    order_status = OrderStatusInFilter(field_name='order_status', lookup_expr='in')

    class Meta:
        model = Order
        fields = [
            "pickup_time", "order_status", "start_time", "end_time",         
        ]
