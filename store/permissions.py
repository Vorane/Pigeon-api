from rest_framework.permissions import IsAuthenticated
from authentication.models import User
from store.models import Attendant


class IsAttendant(IsAuthenticated):
    def has_permission(self, request, view):
        allowed = IsAuthenticated.has_permission(self, request, view)
        if not allowed: return allowed
        try:
            return request.user.is_attendant
        except:
            return False


class IsOutletAttendant (IsAttendant):
    def has_permission(self, request, view):
        is_attendant = IsAttendant.has_permission(self, request, view)
        if not is_attendant: return is_attendant
        print("is attendant");
        try:
            return request.user.attendant.outlet > 0
        except:
            return False

    