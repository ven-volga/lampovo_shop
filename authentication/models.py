from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from authentication.validators import phone_regex, zip_regex


class User(AbstractUser):
    USER_ROLE_CHOICES = [
        ('CU', 'Customer'),
        ('EE', 'Electronic engineer'),
        ('BE', 'Body engineer'),
        ('AM', 'Account manager'),
        ('DEV', 'Developer'),
    ]

    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zip = models.CharField(validators=[zip_regex], max_length=10, blank=True, null=True)
    address = models.CharField(max_length=400, blank=True, null=True)
    role = models.CharField(max_length=4, choices=USER_ROLE_CHOICES, default='CU')
    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that e-mail already exists.")
        },
    )

    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=False,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={},
        validators=[username_validator],
    )

    email_verify = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
