# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from commons.models import BaseModel
from store_listing.models import Outlet
from colorfield.fields import ColorField
from commons.utils import get_image_path
from categories.models import SubCategory
from product_collections.models import Collection

# Create your models here.


class Product(BaseModel):
    name = models.CharField(max_length=256, unique=False)
    display_name = models.CharField(max_length=256, blank=True, null=True)
    thumbnail = models.FileField(
        upload_to=get_image_path, null=True, blank=True)
    description = models.TextField(default="", null=True, blank=True)
    price = models.FloatField(blank=False, null=False, default=0)

    brand = models.CharField(max_length=256, blank=True, null=True)
    size = models.CharField(max_length=256, blank=True, null=True)
    variant = models.CharField(max_length=256, blank=True, null=True)
    color = ColorField(default='#FFFFFF')

    def __str__(self):
        return self.name


class SubCategoryProduct(BaseModel):
    sub_category = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        related_name="subcategory_subcategory_product")
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product_subcategory_product")

    def __str__(self):
        return (str(self.sub_category.store.display_name) + " - " + str(
            self.sub_category.display_name) + " - " + str(
                self.product.display_name))


class CollectionProduct(BaseModel):
    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        related_name="collection_collection_product")
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product_colection_product")

    def __str__(self):
        return (str(self.collection.store.display_name) + " - " + str(
            self.collection.display_name) + " - " + str(
                self.product.display_name))


class Inventory(BaseModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product_inventory_product")
    outlet = models.ForeignKey(
        Outlet,
        on_delete=models.CASCADE,
        related_name="product_outlet_product")
    quantity = models.IntegerField(blank=False, null=False, default=0)
    isOffered = models.BooleanField(default=True, blank=False)

    def __str__(self):
        return (str(self.outlet.display_name) + " - " + str(
            self.product.display_name) + " - " + str(self.quantity))
