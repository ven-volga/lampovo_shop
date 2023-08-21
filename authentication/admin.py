from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from authentication.forms import RegisterUserForm

User = get_user_model()


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    add_fieldsets = (
        (None,
         {
             "classes": ("wide",),
             "fields": ("email", "username", "password1", "password2", "email_verify"),
         },
         ),
    )

    list_display = ("email", "username", "first_name", "last_name", "email_verify", "is_staff")
    list_editable = ()

    add_form = RegisterUserForm
