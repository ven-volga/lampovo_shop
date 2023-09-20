from django.urls import path
from sales.views import OrdersPageView, MainSalesPageView, OrderDetailsView

urlpatterns = [
    path('', MainSalesPageView.as_view(), name='main_sales'),
    path('orders/', OrdersPageView.as_view(), name='orders'),
    path('orders/<int:order_id>/', OrderDetailsView.as_view(), name='order_details'),
]
