from django.shortcuts import render
from rest_framework import generics
from .models import Order, OrderProduct
from .serializers import OrderSerializer, OrderProductSerializer


# Create your views here.
class OrderList(generics.ListAPIView):
    # queryset = Category.objects.all()

    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(is_ordered=True)


class OrderProductList(generics.ListAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderSerializer