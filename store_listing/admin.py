# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from store_listing.models import Store, Outlet, StoreType

# Register your models here.
admin.site.register(Store)
admin.site.register(StoreType)
admin.site.register(Outlet)

