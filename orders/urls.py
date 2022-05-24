from django.urls import path
from .views import OrderList, OrderProductList

urlpatterns = [
    path("order/list/", OrderList.as_view()),
    path("order_product/list/", OrderProductList.as_view())
]