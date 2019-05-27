# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from product_listing.models import Product, SubCategoryProduct, Inventory, CollectionProduct

# Register your models here.
admin.site.register(Product)
admin.site.register(SubCategoryProduct)
admin.site.register(CollectionProduct)
admin.site.register(Inventory)