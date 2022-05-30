from rest_framework import serializers
from .models import Category, Product, Brand, ProductReview, ProductCategory


# category/list/
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = "__all__"
        fields = ["id", "title", "is_active"]


# product-category
class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


# product/get/category_ID/products/
class CategoryProductRetrieveSerializer(serializers.ModelSerializer):
    category_products = CategoryProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'category_products']


# product/all/
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = "__all__"
        fields = ['id', 'title', 'price', 'old_price', 'description', 'quantity', 'brand_id']


# product-preview
class ProductPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'old_price']


# product-reviews
class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'


# product-retrieve info
class ProductRetrieveSerializer(serializers.ModelSerializer):
    reviews = ProductReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'old_price', 'description', 'quantity', 'brand_id', 'reviews']


# product/brand/all/
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'title']


# product-brand
class ProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# product/get/BRAND_ID/ retrieve products
class BrandProductRetrieveSerializer(serializers.ModelSerializer):
    brand_products = ProductBrandSerializer(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = ['id', 'title', 'brand_products']


