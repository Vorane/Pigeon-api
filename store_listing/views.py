# -*- coding: utf-8 -*-
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView, RetrieveAPIView
from store_listing.models import Store, Outlet
from store_listing.serializers import OutletSerializer, StoreSerializer


# Create your views here.
class StoresView(ListCreateAPIView):
    model = Store
    querset = Store.objects.all()
    serializer_class = StoreSerializer


class OutletsView(ListCreateAPIView):
    model = Outlet
    querset = Outlet.objects.all()
    serializer_class = OutletSerializer
