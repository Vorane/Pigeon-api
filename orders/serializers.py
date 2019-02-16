from rest_framework.serializers import ModelSerializer

from store_listing.models import Outlet #Restaurant
from product_listing.models import Product
from product_listing.serializers import ProductSerializer #ProductInlineSerializer
from store_listing.serializers import OutletSerializer #RestaurantInlineSerializer
from orders.models import Order, OrderItem

class OrderInlineSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"




class OrderItemInlineSerializer(ModelSerializer):
    # order = OrderInlineSerializer()
    product = ProductSerializer(
    )

    class Meta:
        model = OrderItem
        fields = ("id", "order", "product", "quantity")

class OrderOrderItemSerializer(ModelSerializer):
    order_order_item  = OrderItemInlineSerializer(many=True,read_only=True)
    class Meta:
        model = Order
        fields = ("order_status" , "comment" , "order_order_item")

class OutletOrdersSerializers(ModelSerializer):
    outlet_order = OrderOrderItemSerializer(many=True, read_only=True)
   
    
    class Meta:
        model = Outlet
<<<<<<< HEAD
        fields = ("id", "outlet_order")
=======
        fields = ("id", "code", "outlet_order")
>>>>>>> 106d9081fba09b4b8232ffe4c3f20ae0cbbc95af

