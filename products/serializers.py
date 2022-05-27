from rest_framework import serializers
from .models import Category, Product, Brand, ProductReview


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


class ProductPreviewSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'old_price']


class ProductReviewSerialazer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'


class ProductRetrieveSerializer(serializers.ModelSerializer):
    reviews = ProductReviewSerialazer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'old_price', 'description', 'quantity', 'brand_id', 'reviews']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'title']

