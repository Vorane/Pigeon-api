from django.conf import settings
from django.conf.urls import url
from product_collections.api import StoreCollectionsView, OutletCollectionsView

app_name = "product_collections"

store_collection_urls = [
    url(r'^$', StoreCollectionsView.as_view(), name="store-collections"),
]
outlet_collection_urls = [
    url(r'^$', OutletCollectionsView.as_view(), name="outlet-collections"),
]