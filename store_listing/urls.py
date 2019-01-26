from django.conf import settings
from django.conf.urls import url
from .views import StoresView, OutletsView

app_name = "storelisting"

store_listing_urls = [
    url(r'^store/', StoresView.as_view(), name='store'),
    url(r'^outlet/', OutletsView.as_view(), name='outlet'),
]
