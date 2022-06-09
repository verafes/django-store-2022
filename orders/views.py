from django.shortcuts import render, HttpResponse
from rest_framework import generics, status

from customers.models import Customer
from products.models import Product
from .models import Order, OrderProduct
from .serializers import OrderSerializer
import json


# Method to update data in Cart - api/order/cart/update
def update_cart(request):
    if request.method == 'POST':
        try:
            request_json = json.loads(request.body)
            customer = Customer.objects.get(token=request_json['token'])
            product = Product.objects.get(pk=request_json['product_id'])
            orders = Order.objects.filter(customer=customer, is_ordered=False).order_by('-id')
            if orders.count() == 0:
                order = Order.objects.create(customer=customer)
            else:
                order = orders[0]

            try:
                product_order = Order.objects.get(product=product)
                if request_json['quantity'] == 0:
                    product_order.delete()
                else:
                    product_order.price = product.price
                    product_order.quantity = request.json['quantity']
                    product_order.save()

            except OrderProduct.DoesNotExist:
                OrderProduct.objects.create(
                    order=order,
                    product=product,
                    price=product.price,
                    quantity=request_json['quantity']
                )
            count_products = OrderProduct.objects.filter(order__customer__token=request_json['token']).count()
            response = {
                'status': True,
                'cart_item_count': count_products
            }
            response_status = status.HTTP_200_OK

            # return HttpResponse(json.dumps(response), status=status.HTTP_200_OK)

            # Homework - create function that returns total quantity

        except BaseException as error:
            response = {
                'status': False,
                'message': str(error)
            }
            response_status = status.HTTP_400_BAD_REQUEST
    else:
        response = {
            'status': False,
            'message': 'Method not allowed. POST required'
        }
        response_status = status.HTTP_405_METHOD_NOT_ALLOWED

    return HttpResponse(json.dumps(response), status=status.HTTP_200_OK)


# List of Orders - api/order/all
class OrderList(generics.ListAPIView):
    # queryset = Category.objects.all()

    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(is_ordered=True)


# List of Products in Order -  orders/get/products/
class OrderProductList(generics.ListAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderSerializer
