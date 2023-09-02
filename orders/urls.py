from django.urls import path

from orders.views import CheckoutView

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('complete/', CheckoutView.as_view(), name='order_complete'),
]
