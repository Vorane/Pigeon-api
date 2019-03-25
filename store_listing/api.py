# -*- coding: utf-8 -*-
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView, RetrieveAPIView
from store_listing.models import Store, Outlet
from store_listing.serializers import OutletSerializer, StoreSerializer, StoreOutletSerializer
from rest_framework.permissions import AllowAny


# Create your views here.
class StoresView(ListCreateAPIView):
    permission_classes = [AllowAny,]
    model = Store
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


class OutletsView(ListCreateAPIView):
    permission_classes = [AllowAny,]
    model = Outlet
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer

class StoreOutletsView(RetrieveAPIView):
    permission_classes = [AllowAny,]
    model = Store
    queryset = Store.objects.all()
    serializer_class = StoreOutletSerializer
    lookup_field="id"