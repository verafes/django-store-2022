from django.urls import path
from .views import OrderList, OrderProductList, update_cart, CartList, OrderFinalize

urlpatterns = [
    path("order/list/", OrderList.as_view()),
    # path("order_product/list/", OrderProductList.as_view()),
    path("cart/update/", update_cart),
    path('cart/list/<slud:customer_tocken>', CartList.as_view()),
    path("finalize/", OrderFinalize.as_view())
]