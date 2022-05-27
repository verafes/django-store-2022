from django.urls import path
from .views import CategoryList, ProductList, BrandList, ProductCreate, ProductRUD, ProductRetrieve

urlpatterns = [
    path("category/list/", CategoryList.as_view()),
    path("all/", ProductList.as_view()),
    path("brand/all/", BrandList.as_view()),
    path("add/", ProductCreate.as_view()),
    path("rud/<int:pk>/", ProductRUD.as_view()),
    path("get/<int:pk>/", ProductRetrieve.as_view())
]