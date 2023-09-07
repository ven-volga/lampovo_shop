from django.urls import path
from main.views import MainPageView, AboutPageView, ShippingPageView,\
    ContactsPageView, PolicyPageView, PaymentMethodsPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('shipping/', ShippingPageView.as_view(), name='shipping'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('policy/', PolicyPageView.as_view(), name='policy'),
    path('pay_methods/', PaymentMethodsPageView.as_view(), name='pay_methods')
]
