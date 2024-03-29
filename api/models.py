# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from commons.models import BaseModel
from store_listing.models import Outlet
import uuid


# Create your models here.
# Paynment transaction model

class PaymentTransaction(models.Model):
    phone_number = models.CharField(max_length=30)
    amount = models.DecimalField(('amount'), max_digits=6, decimal_places=2, default=0)
    isFinished = models.BooleanField(default=False)
    isSuccessFull = models.BooleanField(default=False)
    trans_id = models.CharField(max_length=30)
    order_id = models.CharField(max_length=30)
    checkoutRequestID = models.CharField(max_length=100)
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.phone_number, self.amount)


class Wallet(BaseModel):
    phone_number = models.CharField(max_length=30)
    available_balance = models.DecimalField(('available_balance'), max_digits=6, decimal_places=2, default=0)
    actual_balance = models.DecimalField(('actual_balance'), max_digits=6, decimal_places=2, default=0)
    date_modified = models.DateTimeField(auto_now=True, null=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self):
        return self.phone_number

class OutletWallet(BaseModel):
    outlet = models.ForeignKey(Outlet, on_delete=None, default=0, related_name='outlet_wallet')
    wallet = models.ForeignKey(Wallet, on_delete=None, default=0, related_name='wallet_outlet')


class TransferTransaction(BaseModel):
    source_wallet = models.ForeignKey(Wallet, on_delete=None, default=0, related_name='source_wallet')
    destination_wallet = models.ForeignKey(Wallet, on_delete=None, default=0, related_name='dest_wallet')
    amount = models.DecimalField(('amount'), max_digits=6, decimal_places=2, default=0)
    isFinished = models.BooleanField(default=False)
    isSuccessFull = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {} - Amount : {}".format(self.source_wallet.phone_number, self.destination_wallet.phone_number, self.amount)