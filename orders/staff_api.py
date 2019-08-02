from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from orders.models import Order
from orders.serializers import StaffOrderSerializer
from orders.filters import OrderFilter


class OrdersView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = StaffOrderSerializer
    queryset = Order.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filterset_class = OrderFilter
    model=Order
