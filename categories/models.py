# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from commons.models import BaseModel

# Create your models here.
class Category(BaseModel):
	name = models.CharField(max_length=30, unique=False)
	display_name = models.CharField(max_length=30, blank=True, null=True)
	thumbnail = models.FileField(upload_to=get_image_path, null=True,  blank=True)
	description = models.TextField(default="", null=True)
	color = ColorField(default='#FFFFFF')

	def __str__(self):
		return self.name
