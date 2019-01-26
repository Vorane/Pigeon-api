from django.conf import settings
from django.conf.urls import url
from .api import StoresView, OutletsView, StoreOutletsView

app_name = "storelisting"

store_listing_urls = [
    url(r'^store/$', StoresView.as_view(), name='store'),
    url(r'^store/(?P<id>\d+)/outlets/$', StoreOutletsView.as_view(), name='store-outlet-view'),
    url(r'^outlet/$', OutletsView.as_view(), name='outlet'),
]
