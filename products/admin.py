from django.contrib import admin
from products.models import Product, Category, Brand, ProductCategory, ProductReview


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'old_price', 'description', 'quantity', 'brand_id']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_active']


class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_id', 'category_id']


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'review', 'fullname', 'product_id']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)