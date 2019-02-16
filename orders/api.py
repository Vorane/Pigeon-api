from rest_framework.generics import RetrieveAPIView ,ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.core import serializers

from store_listing.models import Outlet
from product_listing.models import Product
from orders.models import Order, OrderItem
from orders.serializers import OutletOrdersSerializers, OrderOrderItemSerializer, OrderInlineSerializer
import json

def validate_object(my_object, fields):
    for field in fields:
        if not field in my_object.keys():
            return {"status": False, "field": field}
    else:
        return {"status": True}

def calculate_basket_total(items):
    for item_object in items:
        valid = validate_object(item_object, ["id", "quantity"])
    if not valid["status"]:
                return JsonResponse(
                    {
                        'status': 'bad request',
                        'message': "missing attribute: " + valid["field"]
                    },
                    status=400)

class OutletOrdersView(ListAPIView):
    permission_classes = [AllowAny, ]
    model = Outlet
    queryset = Outlet.objects.all()
    serializer_class = OutletOrdersSerializers
    


class OrderDetailsView(RetrieveAPIView):
    permission_classes = [AllowAny, ]
    model = Order
    queryset = Order.objects.all()
    serializer_class = OrderOrderItemSerializer
    lookup_field = "id"



class CreateOrderView(APIView):
    permission_classes = [AllowAny, ]

    # handle the POST method
    serializer_class = OrderInlineSerializer
    def post(self, request, **kwargs):
        if request.data:
            # check if items property exists
            valid = validate_object(request.data, ["items", "comments", "outlet_id", "mpesa_number"])
            if not valid["status"]:
                return JsonResponse(
                    {
                        'status': 'bad request',
                        'message': "missing attribute: " + valid["field"]
                    },
                    status=400)
            #calculate total and send mpesa push sdk to get money for payments
            total_amount = 0 #stores the total amount to be paid
            for item_object in request.data["items"]:
                valid_items = validate_object(item_object, ["product_id", "quantity"]) #check if each item has quantity and product_id values
                if not valid_items["status"]:
                    return JsonResponse(
                        {
                            'status': 'bad request',
                            'message': "missing attribute: " + valid_items["field"]
                        },
                        status=400)
                total_amount += (item_object["quantity"]) * Product.objects.values_list("price", flat=True).get(id=item_object["product_id"])
            print(total_amount)

            # find the outlet making the order
            outlet = Outlet.objects.get(id=request.data["outlet_id"])
            if outlet:

                # create a new order objects
                new_order = Order.objects.create(
                    outlet=outlet, order_status="INITIALIZED", comment=request.data["comments"])
                new_order.save()

                # create the order items
                for item in request.data["items"]:
                    # find the product
                    product = Product.objects.get(id=item["product_id"])

                    if product:

                        # create an order item
                        new_order_item = OrderItem.objects.create(
                            product=product, quantity=item["quantity"], order=new_order)
                        new_order_item.save()
                    else:
                        return JsonResponse(
                            {
                                'status': 'bad request',
                                'message': "product not found"
                            },
                            status=400)

                # success
                # completed
                my_list = OrderOrderItemSerializer(new_order)
                # my_json_list = json.dumps(my_list)
                return JsonResponse(
                    {
                        'status': 'success',
                        'message': "order has been successfully created",
                        "order": my_list.data
                    },
                    status = 201)

            else:
                return JsonResponse(
                    {
                        'status': 'bad request',
                        'message': "outlet not found"
                    },
                    status = 400)

        else:
            return JsonResponse(
                {
                    'status': 'bad request',
                    'message': "request body is missing"
                },
                status = 400)
