from django import forms
from authentication.models import User
from orders.models import Order


class OrderFilterForm(forms.Form):
    order_id = forms.CharField(required=False)
    order_status = forms.ChoiceField(
        choices=[('', '---------')] + list(Order.ORDER_STATUS_CHOICES),
        required=False,
    )
    customer = forms.ModelChoiceField(queryset=User.objects.all(), required=False)


class ChangeStatusForm(forms.Form):
    order_status = forms.ChoiceField(choices=Order.ORDER_STATUS_CHOICES, required=False)
    order_confirm = forms.BooleanField(required=True)


class OrderEditForm(forms.Form):
    pass
