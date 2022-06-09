import uuid

from django.shortcuts import render, HttpResponse
from rest_framework import generics
from .models import Customer, CustomerAddress
from .serializers import CustomerSerializer
import json


# Method to create customer
def customer_create(request):
    if request.method == 'POST':
        try:
            customer_token = str(uuid.uuid4())
            Customer.objects.create(token='')
            response = {
                'status': True,
                'customer_token': customer_token
            }
        except BaseException as error:
            print(error)
            response = {
                'status': False,
                'message': str(error)
            }
    else:
        response = {
            'status': False,
            'message': "Method not allowed. POST required"
        }
    return HttpResponse(json.dumps(response))


# List of Customers - api/customers/all
class CustomerList(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

 #   def get_queryset(self):
 #       return Customer.objects.filter(is_ordered=True)


# List of Customer's Addresses - api/customers/address/all
class CustomerAddressList(generics.ListAPIView):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerSerializer

