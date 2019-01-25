
from rest_framework import serializers
from store_listing.models import Store, Outlet


class OutletSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = "__all__"

class StoreSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"