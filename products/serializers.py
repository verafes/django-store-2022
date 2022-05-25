from rest_framework import serializers
from .models import Category, Product, Brand


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = "__all__"
        fields = ["id", "title", "is_active"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = "__all__"
        fields = ['id', 'title', 'price', 'old_price', 'description', 'quantity', 'brand_id']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'title']
