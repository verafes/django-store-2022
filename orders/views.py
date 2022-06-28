from datetime import datetime

from django.shortcuts import render, HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response

from customers.models import Customer, CustomerAddress
from products.models import Product
from .models import Order, OrderProduct
from .serializers import OrderSerializer, OrderProductSerializer
from customers.serializers import CustomerAddressSerializer
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
            # if no quantity per request, set default by 1
            # if not 'quantity' in request_json:
            #     request_json['quantity'] = 1
            try:
                product_order = OrderProduct.objects.get(product=product, order=order)
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

            # Homework - check the availability of goods in stock
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
            'message': 'Method not allowed. POST required to update cart'
        }
        response_status = status.HTTP_405_METHOD_NOT_ALLOWED

    return HttpResponse(json.dumps(response), status=response_status)


# List of Orders - api/order/all
class OrderList(generics.ListAPIView):
    # queryset = Category.objects.all()

    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(is_ordered=True)


# List of Products in Order - /api/orders/get/products/
class OrderProductList(generics.ListAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderSerializer


# api/order/cart/list/
class CartList(generics.ListAPIView):
    serializer_class = OrderProductSerializer

    def get_queryset(self):
        try:
            return OrderProduct.object.filter(
                order__customer__token=self.kwargs['customer.token'],
                order__is_ordered=False
            )
        except BaseException:
            return None


# api/order/finalize/
class OrderFinalize(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order

    def update(self, request, *args, **kwargs):
        try:
            request_json = request.data
            customer = Customer.object.get(token=request_json['token'])
            order = Order.object.filer(customer=customer, is_ordered=False).order_by('-id')[0]
            serializer = self.get_serializer(order, data=request.data, partial=True)
            serializer.is_valid(raise_exeption=True)
            self.preform_update(serializer)
            customer.first_name = request_json['first_name']
            customer.last_name = request_json['last_name']
            customer.email = request_json['email']
            customer.phone = request_json['phone']

            # home - to check with fields if the address is already created in database,
            # then we do not create it

            address = CustomerAddress.object.create(
                customer=customer,
                country=request_json['country'],
                city=request_json['city'],
                post_code=request_json['post_code'],
                address=request_json['address']
            )

            order.customer_shipping_address = address
            order.is_ordered = True
            order.time_checkout = datetime.now()

            customer.save()
            order.save()

            return Response(serializer.data)

        except BaseException as error:
            return Response({"status": False,
                             "message": str(error)})
