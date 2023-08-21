from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from authentication.utils import send_verify_email

User = get_user_model()


# class UserAuthenticationForm(AuthenticationForm):
#     def clean(self):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#
#         if username is not None and password:
#             self.user_cache = authenticate(
#                 self.request,
#                 username=username,
#                 password=password,
#             )
#             if not self.user_cache.email_verify:
#                 send_verify_email(self.request, self.user_cache)
#                 raise ValidationError(
#                     'Email not verify, check your mailbox',
#                     code='invalid_login'
#                 )
#
#             if self.user_cache is None:
#                 raise self.get_invalid_login_error()
#             else:
#                 self.confirm_login_allowed(self.user_cache)
#
#         return self.cleaned_data


class UserAuthenticationForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password,
            )

            if self.user_cache is None:
                raise self.get_invalid_login_error()

            if not self.user_cache.email_verify:
                send_verify_email(self.request, self.user_cache)
                raise ValidationError(
                    'Email not verified, check your mailbox',
                    code='invalid_login'
                )

            self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "username")

    def clean_username(self):
        username = self.cleaned_data.get("username").capitalize()
        return username

