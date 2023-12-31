from datetime import date
from django.shortcuts import render
from django.views import View
from shop.models import Product
from .forms import SubscriberForm


class MainPageView(View):
    template_name = 'main/index.html'

    def get(self, request):
        products = Product.objects.filter(available=True, is_recommend=True).order_by('id')
        context = {
            'recommend_products': products,
        }

        return render(request, self.template_name, context)


class AboutPageView(View):
    template_name = 'main/about.html'

    def get(self, request):
        return render(request, self.template_name)


class ShippingPageView(View):
    template_name = 'main/shipping.html'

    def get(self, request):
        return render(request, self.template_name)


class ContactsPageView(View):
    template_name = 'main/contacts.html'

    def get(self, request):
        return render(request, self.template_name)


class PolicyPageView(View):
    template_name = 'main/policy.html'

    def get(self, request):
        return render(request, self.template_name)


class PaymentMethodsPageView(View):
    template_name = 'main/pay_methods.html'

    def get(self, request):
        return render(request, self.template_name)


# Old view function with subscriber form (use before start site)
def main_page(request):
    form = SubscriberForm(request.POST or None)
    current_date = date.today()

    context = {
        'form': form,
        'current_date': current_date
    }

    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)

        form.save()

    return render(request, 'main/soon.html', context)
