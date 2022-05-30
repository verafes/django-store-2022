from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser

from .filters import ProductFilter
from .models import Category, Product, Brand
from .serializers import CategorySerializer, ProductSerializer, BrandSerializer, ProductPreviewSerializer, \
    ProductRetrieveSerializer, BrandProductRetrieveSerializer, CategoryProductRetrieveSerializer
from django_filters.rest_framework import DjangoFilterBackend


# api/product/category/list/
class CategoryList(generics.ListAPIView):
    # queryset = Category.objects.all()

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(is_active=True)


# /api/product/get/category_ID/products/
class CategoryProductRetrieve(generics.RetrieveAPIView):
    serializer_class = CategoryProductRetrieveSerializer
    queryset = Category.objects.all()


# api/product/all/
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductPreviewSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    #    filterset_fields = ["title"]
    search_fields = ["title", "brand__title"]
    ordering_fields = ["title", "price"]

    # def get_queryset(self):
    #     return Product.objects.filter(price__gte=900, price__lte=1400)


# api/product/add/
class ProductCreate(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


# api/product/rud/<int:pk>/
class ProductRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdminUser]


# /api/product/get/product_id/
class ProductRetrieve(generics.RetrieveAPIView):
    serializer_class = ProductRetrieveSerializer
    queryset = Product.objects.all()


# api/product/brand/all/
class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


# /api/product/get/BRAND_ID/products/
class ProductBrandRetrieve(generics.RetrieveAPIView):
    serializer_class = BrandProductRetrieveSerializer
    queryset = Brand.objects.all()


# Done:
# api/product/category/list/
# api/product/all/
# api/product/brand/all/  # список брендов
# api/product/add/
# api/product/rud/<int:pk>/
# api/product/get/<int:pk>/
# api/order/
# api/customer/


# Homework
# /api/product/get/category_ID/products/
# /api/product/get/BRAND_ID/products/
