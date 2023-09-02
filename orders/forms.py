from django import forms

from orders.validators import zip_regex, phone_regex


class OrderAddForm(forms.Form):
    country = forms.CharField(label="Country", max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'my-custom-class'}),)
    city = forms.CharField(label="City", max_length=50, required=True)
    zip = forms.CharField(label="ZIP code", max_length=10, required=True, validators=[zip_regex])
    address = forms.CharField(label="Shipping address", max_length=400, required=True)
    phone_number = forms.CharField(label="Phone number", max_length=17, required=True, validators=[phone_regex])
    comment = forms.CharField(label="Order comment", max_length=1000, required=False)
