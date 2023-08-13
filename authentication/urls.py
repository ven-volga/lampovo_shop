from django.urls import path, include
from authentication.views import RegisterUser, UserPage

import django.contrib.auth.urls

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('info/', UserPage.as_view(), name='user'),
    path('', include('django.contrib.auth.urls'))
]
