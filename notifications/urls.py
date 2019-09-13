from django.conf.urls import url, include
from django.contrib import admin
from .api import FCMDeviceView

fcm_urls = [
    url(r'^fcm-device/', FCMDeviceView.as_view(), name='fcm-device'),
]
