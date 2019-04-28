# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from store_listing.models import Store

from colorfield.fields import ColorField
from django.db import models
from commons.models import BaseModel
from commons.utils import get_image_path


# Create your models here.
class Collection(BaseModel):
    name = models.CharField(max_length=30, unique=False)
    display_name = models.CharField(max_length=30, blank=True, null=True)
    thumbnail = models.FileField(
        upload_to=get_image_path, null=True, blank=True)
    description = models.TextField(default="", null=True, blank=True)
    color = ColorField(default='#FFFFFF')
    store = models.ForeignKey(
        Store, on_delete=models.DO_NOTHING, related_name="store_collection")

    def __str__(self):
        return self.name
