from django.conf.urls import url, include

from orders.api import OutletOrdersView, OrderDetailsView, CreateOrderView, UpdateOrdersView, UpdateOrderStatusView

app_name = "orders"

api_outlet_orders_urls = [
    # all products in a restaurant
    url(r'^$', OutletOrdersView.as_view(), name='outlet-products-view'),
    url(r'^create/$',
        CreateOrderView.as_view(),
        name='outlet-create-order-view'),
    url(r'^update_order/(?P<id>\d+)/$',
        UpdateOrdersView.as_view(),
        name='outlet-create-order-view'),
    url(r'^(?P<id>\d+)/$',
        OrderDetailsView.as_view(),
        name='outlet-products-view'),
]

api_orders_urls = [
    url(r'^(?P<id>\d+)/$',
        OrderDetailsView.as_view(),
        name='outlet-products-view'),
    url(r'^update-order-status/',
        UpdateOrderStatusView.as_view(),
        name='retry_transaction'),
]