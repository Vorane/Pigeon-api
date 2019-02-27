from django.conf.urls import url, include
from store_listing.urls import store_listing_urls
from .views import ValidateView, ConfirmView, SubmitView

app_name = "api"

urlpatterns = [
    url(r'^storelisting/', include(store_listing_urls)),
    url(r'^validate/', ValidateView.as_view(), name='validate'),
    url(r'^confirm/', ConfirmView.as_view(), name='confirm'),
    url(r'^submit/', SubmitView.as_view(), name='submit'),
]