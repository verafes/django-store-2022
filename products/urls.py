from django.urls import path
from .views import CategoryList, ProductList

urlpatterns = [
    path("category/list/", CategoryList.as_view()),
    path("product/list/", ProductList.as_view())
]
