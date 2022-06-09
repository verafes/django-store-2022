from rest_framework import serializers
from .models import Order


# List of Order - api/order/list/
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        # fields = "__all__"
        fields = ['id', 'time_created', 'time_checkout', 'time_delivery',
                    'is_ordered', 'customer_id', 'customer_shipping_address_id']


# Products in Order - api/order_product/list/
class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'country', 'city', 'address', 'post_code', 'customer']


