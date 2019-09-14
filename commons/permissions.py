from rest_framework.permissions import IsAuthenticated

from orders.models import OrderItem
from store.models import Attendant


class IsPigeonAttendant(IsAuthenticated):
    def has_permission(self, request, view):
        allowed = IsAuthenticated.has_permission(self, request, view)
        if not allowed: return allowed
        try:
            return request.user.is_pigeon_staff
        except:
            return False
