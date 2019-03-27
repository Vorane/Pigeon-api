from rest_framework.generics import RetrieveAPIView ,ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import JsonResponse
from django.core import serializers
from django_filters.rest_framework import DjangoFilterBackend


from api import mpesa
from store_listing.models import Outlet
from product_listing.models import Product
from orders.models import Order, OrderItem
from api.models import Wallet
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
    permission_classes = [IsAuthenticated, ]
    serializer_class = OrderInlineSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('order_status', 'pickup_time')

    def get_queryset(self):
        """
        Get list of orders for the outlet that the user is assigned to
        """
        user = self.request.user
        return Order.objects.filter(outlet = user.attendant.outlet)



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
            valid = validate_object(request.data, ["items", "comments", "outlet_id", "mpesa_number", "pickup_time"])
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
            #send stk push
            # mpesa_text = mpesa.sendSTK(request.data['mpesa_number'], 50)
            # print(mpesa_text)
            # find the outlet making the order
            outlet = Outlet.objects.get(id=request.data["outlet_id"])
            if outlet:

                # create a new order objects

                phone_number = request.data["mpesa_number"]

                try:
                    wallet = Wallet.objects.filter(phone_number=phone_number).get()
                except Wallet.DoesNotExist:
                    wallet = None 
                if not wallet:
                    wallet = Wallet.objects.create(phone_number=phone_number)
                wallet.save()
                new_order = Order.objects.create(
                    outlet=outlet, order_status="INITIALIZED", comment=request.data["comments"],
                    pickup_time=request.data["pickup_time"], wallet=wallet)
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

                mpesa.sendSTK(request.data["mpesa_number"],total_amount,new_order.id)
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


class UpdateOrdersView(APIView):
    permission_classes = [AllowAny, ]

    # handle the POST method
    serializer_class = OrderInlineSerializer
    def post(self, request, **kwargs):
        if request.data: 
            valid = validate_object(request.data, ["order_status", "pickup_time"])
            if not valid["status"]:
                return JsonResponse(
                    {
                        'status': 'bad request',
                        'message': "missing attribute: " + valid["field"]
                    },
                    status=400)
            #if the request has data
            try:
                order = Order.objects.get(id=kwargs['id'])
            except Order.DoesNotExist:
                order = None 
            #order = Order.objects.get(id=kwargs['id'])
            #get the order with the same id
            if order:
                if request.data["order_status"] != '':
                    order.order_status = request.data["order_status"]
                    order.save()
                elif request.data["pickup_time"] != '':
                    order.pickup_time = request.data["pickup_time"]
                    order.save()
                else:
                    print("no orders to update")
                my_list = OrderOrderItemSerializer(order)
                return JsonResponse(
                    {
                        'status': 'success',
                        'message': "order has been successfully updated",
                        "order": my_list.data
                    },
                    status = 201)
            else:
                return JsonResponse(
                {
                    'status': 'bad request',
                    'message': "order doesnt exist"
                },
                status = 400) 
        else:
            return JsonResponse(
                {
                    'status': 'bad request',
                    'message': "request body is missing"
                },
                status = 400)           






