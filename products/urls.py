from django.urls import path
from .views import CategoryList, ProductList, BrandList, ProductCreate, ProductRUD, ProductRetrieve, \
    ProductBrandRetrieve, CategoryProductRetrieve

urlpatterns = [
    path("category/list/", CategoryList.as_view()),
    path("all/", ProductList.as_view()),
    path("brands/all/", BrandList.as_view()),
    path("add/", ProductCreate.as_view()),
    path("rud/<int:pk>/", ProductRUD.as_view()),
    path("get/<int:pk>/", ProductRetrieve.as_view()),
    path("brands/get/<int:pk>/", ProductBrandRetrieve.as_view()),
    path("category/get/<int:pk>/", CategoryProductRetrieve.as_view())
]


# product/category/CATEGORY_ID/products/
# product/brands/get/BRAND_ID/

# api/product/category/list/
# api/product/all/
# api/product/brands/all/
# api/product/add/
# api/product/rud/<int:pk>/
# api/product/get/<int:pk>/
# api/order/
# api/customer/
