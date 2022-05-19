from django.contrib import admin
from .models import Order, OrderProduct
from products.models import Product

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'time_created', 'time_checkout', 'time_delivery',
                    'is_ordered', 'customer_id', 'customer_shipping_address_id']


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'product_id', 'price', 'quantity']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
