from django.urls import path
from cart import views
from cart.views import CartView

app_name = 'cart'

urlpatterns = [
    # path('', views.cart_detail, name='cart_detail'),
    # path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    # path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),

    path('', CartView.as_view(), name='cart_detail'),
    path('add/<int:product_id>/', CartView.as_view(), name='cart_add'),
    path('remove/<int:product_id>/', CartView.as_view(), name='cart_remove'),
]
