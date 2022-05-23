from django.urls import path
from .views import OrderList

urlpatterns = [
    path("order/list/", OrderList.as_view())
]