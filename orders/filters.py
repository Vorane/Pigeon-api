from django_filters import rest_framework as filters
from django_filters import DateTimeFilter, TimeRangeFilter, IsoDateTimeFilter, DateRangeFilter

from .models import Order

class OrderFilter(filters.FilterSet):
    start_time = IsoDateTimeFilter(field_name='pickup_time',lookup_expr=('gt'),) 
    end_time = IsoDateTimeFilter(field_name='pickup_time',lookup_expr=('lt'))
    

    class Meta:
        model = Order
        fields = ["pickup_time","order_status", "start_time", "end_time"]