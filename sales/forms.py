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

    def __init__(self, *args, **kwargs):
        initial_order_status = kwargs.pop('initial_order_status', None)
        super().__init__(*args, **kwargs)

        if initial_order_status:
            self.fields['order_status'].initial = initial_order_status


class OrderEditForm(forms.Form):
    pass
