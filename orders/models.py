from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models
from commons.models import BaseModel
from product_listing.models import Product
from store_listing.models import Outlet
from commons.utils import validate_object
from commons.app_constants import *
from api.models import Wallet
from django.core.validators import RegexValidator

# Create your models here.


class Order(BaseModel):
    outlet = models.ForeignKey(
        Outlet, on_delete=models.CASCADE, related_name='outlet_order')
    order_status = models.CharField(
        max_length=25, choices=ORDER_STATUSES, default=CREATED)
    comment = models.CharField(max_length=255)
    pickup_time = models.DateTimeField()
    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.DO_NOTHING,
        related_name="order_wallet_order",
        null=True)

    geo = RegexValidator(
        r'^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$'
    )

    delivery_coordinates = models.CharField(
        max_length=50, blank=True, null=True, validators=[geo])
    delivery_address = models.CharField(max_length=256, blank=True, null=True)
    order_contact_person = models.CharField(
        max_length=256, blank=True, null=True)
    recorded_total_amount = models.FloatField(default=0, blank=True, null=True)

    def totalAmount(self):
        order_items = OrderItem.objects.filter(order=self).get()
        total_amount = 0
        for item_object in order_items:
            valid_item = validate_object(
                item_object,
                ["product_id", "quantity"
                 ])  # check if each item has quantity and product_id values
            if valid_item["status"]:
                total_amount += (
                    item_object["quantity"]) * Product.objects.values_list(
                        "price", flat=True).get(id=item_object["product_id"])
        return total_amount

    class Meta:
        ordering = ['-created_at', '-pickup_time']


class OrderItem(BaseModel):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_order_item')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_order_item')
    quantity = models.IntegerField(default=0)