from django.shortcuts import render
from push_notifications.models import GCMDevice
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import FCMDeviceSerializer

# Create your views here.


class FCMDeviceView(ListCreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = FCMDeviceSerializer
    queryset = GCMDevice.objects.all()