import os
from orders.models import Order


def update_order_status(order_id, status):
    try:
        order = Order.objects.filter(id=order_id).get()
        if order:
            order.order_status = status
            order.save()
    except Order.DoesNotExist:
        raise Exception("Order with id {} not found".format(order_id))
