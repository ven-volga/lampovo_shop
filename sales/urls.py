from django.urls import path
from sales.views import OrdersPageView, MainSalesPageView

urlpatterns = [
    path('', MainSalesPageView.as_view(), name='main_sales'),
    path('orders/', OrdersPageView.as_view(), name='orders'),
]
