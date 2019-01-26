
from rest_framework import serializers
from store_listing.models import Store, Outlet


class OutletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = "__all__"

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"