# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Wallet, PaymentTransaction

# Register your models here.
admin.site.register(PaymentTransaction)
admin.site.register(Wallet)