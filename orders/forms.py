from django import forms
from authentication.validators import zip_regex, phone_regex


class OrderAddForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=50, required=True,
                                 widget=forms.TextInput(attrs={'class': 'custom-form'}))
    last_name = forms.CharField(label="Last name", max_length=50, required=True,
                                widget=forms.TextInput(attrs={'class': 'custom-form'}))
    phone_number = forms.CharField(label="Phone number", max_length=17, required=True, validators=[phone_regex],
                                   widget=forms.TextInput(attrs={'class': 'custom-form'}))
    country = forms.CharField(label="Country", max_length=100, required=True,
                              widget=forms.TextInput(attrs={'class': 'custom-form'}))
    city = forms.CharField(label="City", max_length=50, required=True,
                           widget=forms.TextInput(attrs={'class': 'custom-form'}))
    zip = forms.CharField(label="ZIP code", max_length=10, required=True, validators=[zip_regex],
                          widget=forms.TextInput(attrs={'class': 'custom-form'}))
    address = forms.CharField(label="Shipping address", max_length=400, required=True,
                              widget=forms.TextInput(attrs={'class': 'custom-form'}))
    comment = forms.CharField(label="Order comment", max_length=1000, required=False,
                              widget=forms.TextInput(attrs={'class': 'custom-form-area'}))

    def __init__(self, request, *args, **kwargs):
        super(OrderAddForm, self).__init__(*args, **kwargs)
        if request.user.is_authenticated:
            self.fields['first_name'].initial = request.user.first_name
            self.fields['last_name'].initial = request.user.last_name
            self.fields['phone_number'].initial = request.user.phone_number
            self.fields['country'].initial = request.user.country
            self.fields['city'].initial = request.user.city
            self.fields['zip'].initial = request.user.zip
            self.fields['address'].initial = request.user.address
