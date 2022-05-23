from django.shortcuts import render
from rest_framework import generics
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


# Create your views here.
class CategoryList(generics.ListAPIView):
    # queryset = Category.objects.all()

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(is_active=True)


class ProductList(generics.ListAPIView):
    # queryset = Category.objects.all()

    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(category=True)

    