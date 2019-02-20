from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models
from commons.models import  BaseModel 
from product_listing.models import Product
from store_listing.models import Outlet
# Create your models here.

class Order(BaseModel):
    outlet = models.ForeignKey(
        Outlet, on_delete=models.CASCADE, related_name='outlet_order')
    order_status = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    pickup_time = models.DateTimeField(default='2012-09-04 06:00')

class OrderItem(BaseModel):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_order_item')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_order_item')
    quantity = models.IntegerField(default=0)