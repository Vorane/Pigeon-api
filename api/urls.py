from django.conf.urls import url, include
from store_listing.urls import store_listing_urls
from categories.urls import categories_urls

app_name = "api"

urlpatterns = [
    url(r'^storelisting/', include(store_listing_urls)),
    url(r'^categories/', include(categories_urls)),
]