from rest_framework import viewsets
from rest_framework.response import Response

from store_listing.models import Outlet
from store_listing.serializers import OutletSerializer
from .permissions import IsAttendant

class AttendantOutletView(viewsets.ViewSet):
    permission_classes = (IsAttendant,)

    def list(self, request):
        outlet = request.user.attendant.outlet
        serializer = OutletSerializer(outlet, many=False)
        return Response(serializer.data)