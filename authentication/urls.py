from django.urls import path, include
from django.views.generic import TemplateView

from authentication.views import RegisterUserView, UserPageView, EmailVerifyView, LoginUserView

import django.contrib.auth.urls

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('info/', UserPageView.as_view(), name='user'),
    path('confirm_email/', TemplateView.as_view(
        template_name='registration/confirm_email.html'), name='confirm_email'),
    path(
        'verify_email/<uidb64>/<token>/',
        EmailVerifyView.as_view(),
        name='verify_email'
    ),
    path('invalid_verify/', TemplateView.as_view(
        template_name='registration/invalid_verify.html'), name='invalid_verify'),
    path('', include('django.contrib.auth.urls'))
]
