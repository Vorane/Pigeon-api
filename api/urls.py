from django.conf.urls import url, include
from store_listing.urls import store_listing_urls
from orders.urls import api_orders_urls as orders_urls
from .views import ValidateView, ConfirmView, SubmitView, CheckTransaction, RetryTransaction

from store.urls import store_urls

app_name = "api"

urlpatterns = [
    url(r'^storelisting/', include(store_listing_urls)),
    url(r'^store/', include(store_urls)),
    url(r'^orders/', include(orders_urls)),
    url(r'^validate/', ValidateView.as_view(), name='validate'),
    url(r'^confirm/', ConfirmView.as_view(), name='confirm'),
    url(r'^submit/', SubmitView.as_view(), name='submit'),
    url(r'^checktransaction/', CheckTransaction.as_view(), name='check_transaction'),
    url(r'^retrytransaction/', RetryTransaction.as_view(), name='retry_transaction'),

]