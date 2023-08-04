from django.contrib.auth import logout
from django.shortcuts import render, redirect


def login_user(request):
    return render(request, 'auth/login.html')


def register_user(request):
    return render(request, 'auth/register.html')


def user_page(request):
    return render(request, 'auth/user.html')


def logout_user(request):
    logout(request)
    return redirect('main_page')
