# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from categories.models import Category, SubCategory, CategorySubCategory

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(CategorySubCategory)
