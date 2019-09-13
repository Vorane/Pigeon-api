from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import ObtainJSONWebToken,obtain_jwt_token, refresh_jwt_token
from .custom_auth import CustomJWTSerializer

auth_urls = [
    url(r'api-token-auth/', ObtainJSONWebToken.as_view(serializer_class=CustomJWTSerializer)),
    url(r'^api-token-refresh/', refresh_jwt_token),
]
