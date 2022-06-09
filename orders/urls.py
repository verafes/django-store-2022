from django.urls import path
from .views import OrderList, OrderProductList, update_cart

urlpatterns = [
    path("order/list/", OrderList.as_view()),
    path("order_product/list/", OrderProductList.as_view()),
    path("cart/update/", update_cart)
]