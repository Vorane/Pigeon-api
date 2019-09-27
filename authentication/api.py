from __future__ import unicode_literals

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import AccountCreateSerializer


class UserCreateAPIView(CreateAPIView):
    """ create user"""
    permission_classes = [AllowAny, ]
    serializer_class = AccountCreateSerializer
