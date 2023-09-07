from django.urls import path
from sales.views import OrdersPageView

urlpatterns = [
    path('orders/', OrdersPageView.as_view(), name='orders'),
]
