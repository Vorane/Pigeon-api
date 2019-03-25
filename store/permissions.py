from rest_framework.permissions import IsAuthenticated
from authentication.models import User

class IsAttendant (IsAuthenticated):
    def has_permission(self, request, view):
        allowed = IsAuthenticated.has_permission(self, request, view)
        if not allowed: return allowed
        try:
            request.user.attendant
            return True
        except:
            return False

    