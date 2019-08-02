from rest_framework.serializers import ModelSerializer

from store_listing.models import Outlet  #Restaurant
from product_listing.models import Product
from product_listing.serializers import ProductSerializer, ProductInventorySerializer  #ProductInlineSerializer
from store_listing.serializers import OutletInlineSerializer, OutletSerializer  #RestaurantInlineSerializer
from orders.models import Order, OrderItem
from api.serializers import WalletInlineSerializer


class OrderInlineSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemInlineSerializer(ModelSerializer):
    # order = OrderInlineSerializer()
    product = ProductInventorySerializer()

    class Meta:
        model = OrderItem
        fields = ("id", "order", "product", "quantity")


#TODO swap out with orderItemInlineSerializer
class OrderItemSerializer(ModelSerializer):
    # order = OrderInlineSerializer()
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ("id", "order", "product", "quantity")


class OrderOrderItemSerializer(ModelSerializer):
    order_order_item = OrderItemInlineSerializer(many=True, read_only=True)
    outlet = OutletInlineSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ("id", "order_status", "comment", "pickup_time",
                  "order_order_item", "outlet", "delivery_coordinates",
                  "delivery_address", "order_contact_person")


class OrderDetailSerializer(ModelSerializer):
    order_order_item = OrderItemInlineSerializer(many=True, read_only=True)
    outlet = OutletInlineSerializer(read_only=True)
    wallet = WalletInlineSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ("id", "order_status", "comment", "pickup_time",
                  "order_order_item", "outlet", "delivery_coordinates",
                  "delivery_address", "order_contact_person", "wallet")


class StaffOrderSerializer(ModelSerializer):
    order_order_item = OrderItemSerializer(many=True, read_only=True)
    outlet = OutletSerializer(read_only=True)
    wallet = WalletInlineSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ("id", "order_status", "comment", "pickup_time",
                  "order_order_item", "outlet", "delivery_coordinates",
                  "delivery_address", "order_contact_person", "wallet")


class OutletOrdersSerializers(ModelSerializer):
    outlet_order = OrderOrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Outlet

        fields = ("id", "outlet_order")
