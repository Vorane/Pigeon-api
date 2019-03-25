from django.conf import settings
from django.conf.urls import url, include
from .api import AttendantOutletView


app_name = "store"

store_urls = [
    url(r'^outlet/', AttendantOutletView.as_view({'get': 'list'}), name="attendant-outlet-view" ),    
]
