# -*- coding: utf-8 -*-
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from django_filters.rest_framework import DjangoFilterBackend
from store_listing.models import Store, Outlet, StoreType
from store_listing.serializers import (
    OutletSerializer,
    StoreSerializer,
    StoreOutletSerializer,
    StoreTypeSerializer,
)
from rest_framework.permissions import AllowAny
from .filters import OutletFilter


# Create your views here.
class StoresView(ListCreateAPIView):
    permission_classes = [AllowAny]
    model = Store
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


class OutletsView(ListCreateAPIView):
    permission_classes = [AllowAny]
    model = Outlet
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OutletFilter


class StoreOutletsView(RetrieveAPIView):
    permission_classes = [AllowAny]
    model = Store
    queryset = Store.objects.all()
    serializer_class = StoreOutletSerializer
    lookup_field = "id"


class StoreTypesView(ListAPIView):
    permission_classes = [AllowAny]
    model = StoreType
    queryset = StoreType.objects.all()
    serializer_class = StoreTypeSerializer

