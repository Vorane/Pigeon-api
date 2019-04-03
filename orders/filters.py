from django_filters import rest_framework as filters
from django_filters import DateTimeFilter, TimeRangeFilter, IsoDateTimeFilter

from .models import Order

class OrderFilter(filters.FilterSet):
    start_time = IsoDateTimeFilter(field_name='pickup_time',lookup_expr=('gt'),) 
    end_time = IsoDateTimeFilter(field_name='pickup_time',lookup_expr=('lt'))
    time_range = TimeRangeFilter(field_name='pickup_time')

    class Meta:
        model = Order
        fields = ["pickup_time","order_status", "start_time", "end_time", "time_range"]