import uuid, os
from orders.models import Order


def get_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(instance._meta.db_table, filename)


def validate_object(my_object, fields):
    for field in fields:
        if not field in my_object.keys():
            return {"status": False, "field": field}
    else:
        return {"status": True}


def update_order_status(order_id, status):
    try:
        order = Order.objects.filter(id=order_id).get()
        if order:
            order.order_status = status
            order.save()
    except Order.DoesNotExist:
        raise Exception("Order with id {} not found".format(order_id))


class OrderUtils:
    CREATED = 'CRT'
    AWAITING_FUNDS = 'AWF'
    INSUFFICIENT_FUNDS_FAILURE = 'IFF'
    READY_FOR_PROCESSING = 'RFP'
    IN_PROCESSING = 'IPR'
    AWAITING_SUBSTITUTION = 'ASC'
    IN_CHECKOUT = 'ICH'
    CANCELLED_BY_USER = 'CUS'
    READY_FOR_PICKUP = 'RPK'
    PICKED = 'PKD'
    NOT_PICKED = 'NPK'

    ORDER_STATUSES = (
        (CREATED, 'Created'),
        (AWAITING_FUNDS, 'Awaiting Funds'),
        (INSUFFICIENT_FUNDS_FAILURE, 'Insufficient Funds Failure'),
        (READY_FOR_PROCESSING, 'Ready For Processing'),
        (IN_PROCESSING, 'In Processing'),
        (AWAITING_SUBSTITUTION, 'Awaiting Substitution Consent'),
        (IN_CHECKOUT, 'In Checkout'),
        (CANCELLED_BY_USER, 'Cancelled By User'),
        (READY_FOR_PICKUP, 'Ready For Pickup'),
        (PICKED, 'Picked'),
        (NOT_PICKED, 'Not Picked'),
    )
