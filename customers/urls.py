from django.urls import path

from orders.views import update_cart
from .views import *       # * - all methods

urlpatterns = [
    path("list/", CustomerList.as_view()),
    path("address/list/", CustomerAddressList.as_view()),
    path("create/", customer_create)
]