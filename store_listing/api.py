# -*- coding: utf-8 -*-
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView, RetrieveAPIView
from store_listing.models import Store, Outlet
from store_listing.serializers import OutletSerializer, StoreSerializer, StoreOutletSerializer


# Create your views here.
class StoresView(ListCreateAPIView):
    model = Store
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


class OutletsView(ListCreateAPIView):
    model = Outlet
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer

class StoreOutletsView(RetrieveAPIView):
    model = Store
    queryset = Store.objects.all()
    serializer_class = StoreOutletSerializer
    lookup_field="id"