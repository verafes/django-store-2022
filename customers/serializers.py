from rest_framework import serializers
from .models import Customer, CustomerAddress


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        #fields = ["id", "title", "is_active"]


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        