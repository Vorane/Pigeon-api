from rest_framework.permissions import IsAuthenticated

from authentication.models import User
from store_listing.models import Outlet


class IsAllowedInventoryUpdate(IsAuthenticated):
    #check if the request user is in the same outlet as the product inventory
    def has_object_permission(self, request, view, obj):
        allowed = IsAuthenticated.has_permission(self, request, view)
        if not allowed: return allowed
        try:
            request.user.attendant
            return obj.outlet == request.user.attendant.outlet
        except:
            return False
