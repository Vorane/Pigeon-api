from django.conf import settings
from django.conf.urls import url, include
from .api import StoresView, OutletsView, StoreOutletsView


from categories.urls import store_categories_urls

app_name = "storelisting"

store_listing_urls = [
    url(r'^store/$', StoresView.as_view(), name='store'),
    url(r'^store/(?P<id>\d+)/outlets/$', StoreOutletsView.as_view(), name='store-outlet-view'),
    url(r'^store/(?P<id>\d+)/categories/', include(store_categories_urls)),
    url(r'^outlet/$', OutletsView.as_view(), name='outlet'),

    
]
