from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from authentication.forms import RegisterUserForm
from django.utils.translation import gettext_lazy as _

User = get_user_model()


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("username", "first_name", "last_name", "phone_number")}),
        (_("Shipment info"), {"fields": ("country", "city", "zip", "address")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "role")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None,
         {
             "classes": ("wide",),
             "fields": ("email", "username", "password1", "password2", "email_verify"),
         },
         ),
    )

    list_display = ("email", "username", "first_name", "last_name", "email_verify", "is_staff",)
    list_editable = ()
    list_filter = ("is_staff", "is_superuser", "is_active", "groups", "role")
    search_fields = ("username", "first_name", "last_name", "email")

    add_form = RegisterUserForm
