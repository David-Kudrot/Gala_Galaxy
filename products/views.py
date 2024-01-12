from django.shortcuts import render
from products.models import CategoryModel, ProductModel
from .serializers import CategorySerializer, ProductSerializer
from rest_framework import viewsets


class CategorySerializerViewsets(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    

class ProductSerializerViewsets(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer



