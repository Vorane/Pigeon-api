from django_filters import rest_framework as filters
from django_filters import (
    DateTimeFilter,
    TimeRangeFilter,
    IsoDateTimeFilter,
    DateRangeFilter,
    BaseInFilter,
    CharFilter,
)

from .models import Outlet


class OutletFilter(filters.FilterSet):
    store__store_type__service_type = CharFilter(lookup_expr="icontains")

    class Meta:
        model = Outlet
        fields = ["name", "display_name", "location", "store"]

