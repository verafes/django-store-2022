from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Brand(models.Model):
    class Meta:
        db_table = "brand"
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    title = models.CharField(verbose_name="Title", max_length=200, blank=False, null=False)

    def __str__(self):
        return self.title


class Product(models.Model):
    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    user = models.ForeignKey(User, verbose_name="Owner", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title", max_length=200, blank=False, null=False)
    price = models.DecimalField(verbose_name="Price", default=0, decimal_places=2, max_digits=10)
    old_price = models.DecimalField(verbose_name="Old Price", default=0, decimal_places=2, max_digits=10, null=False)
    description = models.CharField(verbose_name="Description", max_length=100000, blank=False, null=False)
    quantity = models.DecimalField(verbose_name="Quantity", default=0, decimal_places=2, max_digits=4, null=False)
    image = models.ImageField(verbose_name="Image", upload_to='images/', null=True, blank=True)
    brand = models.ForeignKey(Brand, verbose_name="Brand", on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.title


class Category(models.Model):
    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    title = models.CharField(verbose_name="Title", max_length=200, blank=False, null=False)
    is_active = models.BooleanField(verbose_name="Title", default=False, blank=False, null=False)

    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    class Meta:
        db_table = "product_category"
        verbose_name = "Product Category"
        verbose_name_plural = "Products Categories"

    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE, blank=False, null=False)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f"for '{self.product}' product"


class ProductReview(models.Model):
    class Meta:
        db_table = "product_review"
        verbose_name = "Product review"
        verbose_name_plural = "Products reviews"

    review = models.CharField(verbose_name="Review", max_length=200000, blank=False, null=False)
    fullname = models.CharField(verbose_name="Full name", max_length=200, blank=False, null=False)
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.fullname
