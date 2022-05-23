from django.urls import path
from .views import CustomerList, CustomerAddressList

urlpatterns = [
    path("customer/list/", CustomerList.as_view()),
    path("address/list/", CustomerAddressList.as_view())
]