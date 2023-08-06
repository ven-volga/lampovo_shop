from django.urls import path
from authentication import views


urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('user/', views.user_page, name='user'),
    path('logout/', views.logout_user, name='logout'),
]
