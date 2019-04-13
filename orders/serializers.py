from rest_framework.serializers import ModelSerializer

from store_listing.models import Outlet  #Restaurant
from product_listing.models import Product
from product_listing.serializers import ProductSerializer  #ProductInlineSerializer
from store_listing.serializers import OutletInlineSerializer  #RestaurantInlineSerializer
from orders.models import Order, OrderItem


class OrderInlineSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemInlineSerializer(ModelSerializer):
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
                  "order_order_item", "outlet")


class OrderDetailSerializer(ModelSerializer):
    order_order_item = OrderItemInlineSerializer(many=True, read_only=True)
    outlet = OutletInlineSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ("order_status", "comment", "pickup_time", "order_order_item",
                  "outlet")


class OutletOrdersSerializers(ModelSerializer):
    outlet_order = OrderOrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Outlet

        fields = ("id", "outlet_order")
