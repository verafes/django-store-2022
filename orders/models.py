from django.db import models
from customers.models import CustomerAddress, Customer
from products.models import Product


class Order(models.Model):
    class Meta:
        db_table = "order"
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    customer_id = models.ForeignKey(Customer, verbose_name="Product", on_delete=models.CASCADE, blank=False, null=False)
    customer_shipping_address_id = models.ForeignKey(CustomerAddress, verbose_name="Product", on_delete=models.CASCADE, blank=False, null=False)
    time_created = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    time_checkout = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    time_delivery = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    is_ordered = models.BooleanField(verbose_name="Title", default=False, blank=False, null=False)


class OrderProduct(models.Model):
    class Meta:
        db_table = "order_product"
        verbose_name = "Order Product"
        verbose_name_plural = "Order Products"

    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE, blank=False, null=False)
    order = models.ForeignKey(Order, verbose_name="Order", on_delete=models.CASCADE, blank=False, null=False)
    price = models.DecimalField(verbose_name="Price", default=0, decimal_places=2, max_digits=10)
    quantity = models.DecimalField(verbose_name="Quantity", default=0, decimal_places=2, max_digits=5)

