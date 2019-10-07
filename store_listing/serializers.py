from rest_framework import serializers
from store_listing.models import Store, Outlet, StoreType


class OutletInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = ("id", "name", "display_name")


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
        fields = ("id", "name", "outlets")


class StoreTypeInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreType
        fields = ("id", "name", "display_name")


class StoreTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreType
        fields = "__all__"
