from django.shortcuts import render
from rest_framework import generics, filters

from .filters import ProductFilter
from .models import Category, Product, Brand
from .serializers import CategorySerializer, ProductSerializer, BrandSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class CategoryList(generics.ListAPIView):
    # queryset = Category.objects.all()

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(is_active=True)


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
#    filterset_fields = ["title"]
    search_fields = ["title", "brand__title"]
    ordering_fields = ["title", "price"]

    # def get_queryset(self):
    #     return Product.objects.filter(price__gte=900, price__lte=1400)


class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


