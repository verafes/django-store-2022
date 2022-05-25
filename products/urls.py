from django.urls import path
from .views import CategoryList, ProductList, BrandList

urlpatterns = [
    path("category/list/", CategoryList.as_view()),
    path("all/", ProductList.as_view()),
    path("brand/all/", BrandList.as_view())
]