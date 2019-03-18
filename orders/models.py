from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models
from commons.models import  BaseModel 
from product_listing.models import Product
from store_listing.models import Outlet
from commons.utils import validate_object
from api.models import Wallet
# Create your models here.

class Order(BaseModel):
    outlet = models.ForeignKey(
        Outlet, on_delete=models.CASCADE, related_name='outlet_order')
    order_status = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    pickup_time = models.DateTimeField(default='2012-09-04 06:00')
    wallet = models.ForeignKey(Wallet, on_delete=models.DO_NOTHING, related_name="order_wallet_order", null=True)


    def totalAmount(self):
        order_items = OrderItem.objects.filter(order=self).get()
        total_amount = 0
        for item_object in order_items:
            valid_item = validate_object(item_object, ["product_id","quantity"])  # check if each item has quantity and product_id values
            if valid_item["status"]:
                total_amount += (item_object["quantity"]) * Product.objects.values_list("price", flat=True).get(id=item_object["product_id"])
        return total_amount



class OrderItem(BaseModel):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_order_item')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_order_item')
    quantity = models.IntegerField(default=0)