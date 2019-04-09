
from rest_framework import serializers
from store_listing.models import Store, Outlet


class OutletInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = ('id',"name",'display_name')

class OutletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = "__all__"

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"

class StoreOutletSerializer(serializers.ModelSerializer):
    outlets = OutletSerializer(many=True, source="store_outlet")
    class Meta:
        model = Store
        fields=("id","name","outlets")