from rest_framework.permissions import IsAuthenticated
from authentication.models import User
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from orders.models import OrderItem
from store.models import Attendant


class IsAttendant(IsAuthenticated):
    def has_permission(self, request, view):
        allowed = IsAuthenticated.has_permission(self, request, view)
        if not allowed: return allowed
        try:
            return request.user.is_attendant
        except:
            return False


class IsInOutlet(IsAuthenticated):
    def has_permission(self, request, view):
        is_attendant = IsAttendant.has_permission(self, request, view)
        if not is_attendant: return is_attendant
        order_id = request.resolver_match.kwargs.get('order_item_id')
        try:
            order_item = OrderItem.objects.get(id=order_id)
            attendant = Attendant.objects.get(user=request.user)
            return  order_item.order.outlet == attendant.outlet
        except:
            return True
