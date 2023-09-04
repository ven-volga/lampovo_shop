from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.views import View
from authentication.forms import RegisterUserForm, UserAuthenticationForm
from authentication.utils import send_verify_email
from django.contrib.auth.tokens import default_token_generator as token_generator

from orders.models import Order

User = get_user_model()


class LoginUserView(LoginView):
    form_class = UserAuthenticationForm


class EmailVerifyView(View):
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('main_page')
        return redirect('invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            User.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user


class RegisterUserView(View):
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
            send_verify_email(request, user)
            return redirect('confirm_email')

        context = {'register_form': register_form}
        return render(request, self.template_name, context)


class UserPageView(View):
    template_name = 'registration/user.html'
    template_redirect = 'registration/login.html'

    def get(self, request):
        if request.user.is_authenticated and request.user.role in ('Customer', 'CU', None):
            orders = Order.get_order_info(request.user.id)

            context = {
                'orders': orders,
            }

            return render(request, self.template_name, context)
        else:
            return render(request, self.template_redirect)
