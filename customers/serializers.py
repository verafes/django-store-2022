from rest_framework import serializers
from .models import Customer, CustomerAddress


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        #fields = "__all__"
        fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'time_created', 'user_id']


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = "__all__"
        fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'time_created', 'user_id']

