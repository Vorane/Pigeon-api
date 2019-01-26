# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from colorfield.fields import ColorField
from commons.utils import get_image_path
from commons.models import BaseModel


# Create your models here.

class Store(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    display_name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to=get_image_path)
    website = models.CharField(null=True, blank=True, max_length=50)
    telephone = models.CharField(null=True, blank=True, max_length=50)
    email = models.EmailField(null=True, blank=True, max_length=50)
    color = ColorField(default='#FFFFFF')

    def __str__(self):
        return self.name


class Outlet(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    display_name = models.CharField(blank=True, null=True, max_length=50)
    latitude = models.DecimalField(max_digits=12, decimal_places=8, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=8, null=True)
    working_hours = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    location = models.CharField(max_length=255, null=True)
    telephone = models.CharField(max_length=30, null=True)
    website = models.CharField(max_length=30, null=True)
    store = models.ForeignKey(Store, on_delete=models.DO_NOTHING, related_name="store_outlet")

    def __str__(self):
        return self.name
