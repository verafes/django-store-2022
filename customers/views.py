from django.shortcuts import render
from rest_framework import generics
from .models import Customer, CustomerAddress
from .serializers import CustomerSerializer


# Create your views here.
class CustomerList(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

 #   def get_queryset(self):
 #       return Customer.objects.filter(is_ordered=True)


class CustomerAddressList(generics.ListAPIView):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerSerializer

