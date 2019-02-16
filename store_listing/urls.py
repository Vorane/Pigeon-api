from django.conf import settings
from django.conf.urls import url, include
from .api import StoresView, OutletsView, StoreOutletsView
from product_listing.api import ProductListView , InventoryListView

from categories.urls import store_categories_urls
from orders.urls import api_outlet_orders_urls
from product_listing.urls import api_product_urls
app_name = "storelisting"

store_listing_urls = [
    url(r'^store/$', StoresView.as_view(), name='store'),
    url(r'^store/(?P<id>\d+)/outlets/$', StoreOutletsView.as_view(), name='store-outlet-view'),
    url(r'^store/(?P<id>\d+)/categories/', include(store_categories_urls)),
    url(r'^outlet/$', OutletsView.as_view(), name='outlet'),
    url(r'^store/(?P<id>\d+)/orders/', include(api_outlet_orders_urls)),
    url(r'^store/(?P<id>\d+)/inventory/', include(api_product_urls)),
    url(r'^products/', ProductListView.as_view(), name='outlet-products-view'),

    
]
