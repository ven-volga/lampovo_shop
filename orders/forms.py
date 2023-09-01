from django import forms


class OrderAddForm(forms.Form):
    shipping = forms.CharField(label="Shipping address", max_length=1000)
