from rest_framework.generics import RetrieveAPIView
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

class OutletOrdersView(RetrieveAPIView):
    permission_classes = [AllowAny, ]
    model = Outlet
    queryset = Outlet.objects.all()
    serializer_class = OutletOrdersSerializers
    lookup_field = "code"


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
            valid = validate_object(request.data, ["items", "comments"])
            if not valid["status"]:
                return JsonResponse(
                    {
                        'status': 'bad request',
                        'message': "missing attribute: " + valid["field"]
                    },
                    status=400)

            # find the outlet making the order
            outlet = Outlet.objects.get(code=kwargs['code'])
            if oulet:

                # create a new order objects
                new_order = Order.objects.create(
                    outlet=outlet, order_status="INITIALIZED", comment=request.data["comments"])
                new_order.save()

                # create the order items
                for item in request.data["items"]:
                    # find the product
                    product = Product.objects.get(id=item["product"])

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
