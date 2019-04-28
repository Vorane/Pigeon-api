from django.conf import settings
from django.conf.urls import url
from product_collections.api import StoreCollectionsView

app_name = "product_collections"

store_collection_urls = [
    url(r'^$', StoreCollectionsView.as_view(), name="store-collections"),
]