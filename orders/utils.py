from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def send_order_email(request, user):
    current_site = get_current_site(request)
    context = {
        "user": user,
        "domain": current_site.domain,
    }
    message = render_to_string(
        'shop/order_complete_email.html',
        context=context,
    )
    email = EmailMessage(
        'Order complete email',
        message,
        to=[user.email]
    )
    email.send()
