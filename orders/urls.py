from django.conf.urls import url, include

from orders.api import OutletOrdersView, OrderDetailsView, CreateOrderView, UpdateOrdersView, UpdateOrderStatusView, AddItemToOrderView, RemoveOrderItemView, SwapOutOrderItemView
from orders.staff_api import OrdersView

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
    url(r'^add-item/',
        AddItemToOrderView.as_view(),
        name='add_order_item'),
    url(r'^order-item/(?P<order_item_id>\d+)/remove/$',
        RemoveOrderItemView.as_view()),
    url(r'^order-item/(?P<order_item_id>\d+)/swap-out/$',
        SwapOutOrderItemView.as_view())
]

api_orders_staff_urls = [
    url(r'^$', OrdersView.as_view(), name='order-list-view'),
    url(r'^update_order/(?P<id>\d+)/$',UpdateOrderStatusView.as_view(), name='staff-orders-update'),
]
