from django.db import models
from products.models import User


class Customer(models.Model):
    class Meta:
        db_table = "customer"
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    first_name = models.CharField(verbose_name="First Name", max_length=200, blank=False, null=False)
    last_name = models.CharField(verbose_name="Last Name", max_length=200, blank=False, null=False)
    phone = models.BigIntegerField(verbose_name="Phone number")
    email = models.CharField(verbose_name="Email", max_length=200, blank=False, null=False)
    time_created = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    user = models.ForeignKey(User, verbose_name="Owner", on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name, self.last_name


class CustomerAddress(models.Model):
    class Meta:
        db_table = "customer_address"
        verbose_name = "Customer Address"
        verbose_name_plural = "Customers Addresses"

    country = models.CharField(verbose_name="Country", max_length=60, blank=False, null=False)
    city = models.CharField(verbose_name="City", max_length=30, blank=False, null=False)
    address = models.CharField(verbose_name="Address", max_length=200, blank=False, null=False)
    post_code = models.CharField(verbose_name="Post code", max_length=10, blank=False, null=False)
    customer = models.ForeignKey(Customer, verbose_name="Customer Address", on_delete=models.CASCADE, blank=False, null=False)

