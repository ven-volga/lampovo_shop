from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.shortcuts import render, redirect
from django.views import View

from authentication.forms import RegisterUserForm


class RegisterUser(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'register_form': RegisterUserForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        register_form = RegisterUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('main_page')

        context = {'register_form': register_form}
        return render(request, self.template_name, context)


class UserPage(View):
    template_name = 'registration/user.html'

    def get(self, request):
        return render(request, self.template_name)
