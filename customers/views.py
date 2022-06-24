import uuid
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework import generics

from orders.models import Order
from .models import Customer, CustomerAddress
from .serializers import CustomerSerializer, UserSerializer, MyOrderSerializer
from django.contrib.auth import get_user_model
import json


User = get_user_model()

# Method to create customer
def customer_create(request):
    if request.method == 'POST':
        try:
            customer_token = str(uuid.uuid4())
            Customer.objects.create(token=customer_token)
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


# List of Customers - api/customer/list
class CustomerList(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

 #   def get_queryset(self):
 #       return Customer.objects.filter(is_ordered=True)


# List of Customer's Addresses - api/customer/address/list
class CustomerAddressList(generics.ListAPIView):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerSerializer


class GetAuthCustomer(generics.RetrieveAPIView):
    serializer_class = CustomerSerializer
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get_object(self):
        print("USER", self.request.user)
        customer = get_object_or_404(Customer, user=self.request.user)
        # customer = Customer.objects.get(user=self.request.user)
        print("CUSTOMER:", customer)
        return customer


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User


class MyOrders(generics.ListAPIView):
    serializer_class = MyOrderSerializer
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Order.objects.filter(customer__user=self.request.user)