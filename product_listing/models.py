# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from commons.models import BaseModel
from colorfield.fields import ColorField
from commons.utils import get_image_path
from categories.models import SubCategory

# Create your models here.


class Product(BaseModel):
    name = models.CharField(max_length=30, unique=False)
    display_name = models.CharField(max_length=30, blank=True, null=True)
    thumbnail = models.FileField(upload_to=get_image_path, null=True, blank=True)
    description = models.TextField(default="", null=True, blank=True)
    price = models.FloatField( blank=False, null=False , default=0)

    brand = models.CharField(max_length=30, blank=True, null=True)
    size = models.CharField(max_length=30, blank=True, null=True)
    variant = models.CharField(max_length=30, blank=True, null=True)
    color = ColorField(default='#FFFFFF')

    def __str__(self):
        return self.name


class SubCategoryProduct(BaseModel):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="subcategory_subcategory_product")
    product  = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_subcategory_product")