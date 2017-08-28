# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from product.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):

    fields = ('name',)


class ProductAdmin(admin.ModelAdmin):

    fields = ('name', 'category',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

# Register your models here.
