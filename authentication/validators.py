from django.core.validators import RegexValidator

zip_regex = RegexValidator(
    regex='^\d{3,10}$',
    message='ZIP code must consist only of digits and contain between 3 and 10 characters.',
)

phone_regex = RegexValidator(
    regex=r'^\+\d{9,15}$',
    message='Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.',
)
