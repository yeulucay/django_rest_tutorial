# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from serializers import CategorySerializer,ProductSerializer,ProductPostSerializer
from models import Category, Product
from rest_framework.decorators import api_view
from rest_framework.mixins import ListModelMixin

class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        q = self.request.query_params.get('q', '')
        return Category.objects.filter(name__startswith=q)


class ProductView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()


class ProductPostView(generics.CreateAPIView):

    serializer_class = ProductPostSerializer

    #def post(self, request, *args, **kwargs):
    #    print self.request.data

# Create your views here.
