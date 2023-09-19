from django.shortcuts import render, redirect
from django.views import View
from orders.models import Order, OrderItem
from sales.forms import OrderFilterForm


class MainSalesPageView(View):
    template_name = 'sales/main.html'

    def get(self, request):
        if request.user.is_authenticated and request.user.role not in ('CU', ):
            orders = Order.objects.all()
            order_data = []

            context = {
                'order_data': order_data,
                'orders': orders,
            }

            return render(request, self.template_name, context)

        else:
            return redirect('main_page')


class OrdersPageView(View):
    template_name = 'sales/orders.html'

    def get(self, request):
        if request.user.is_authenticated and request.user.role not in ('CU',):
            form = OrderFilterForm(request.GET)
            orders = Order.objects.all()

            if form.is_valid():
                order_id = form.cleaned_data.get('order_id')
                order_status = form.cleaned_data.get('order_status')
                customer = form.cleaned_data.get('customer')

                if order_id:
                    orders = orders.filter(order_id=order_id)

                if order_status:
                    orders = orders.filter(order_status=order_status)

                if customer:
                    orders = orders.filter(customer=customer)

            context = {
                'form': form,
                'orders': orders,
            }

            return render(request, self.template_name, context)

        return redirect('main_page')


class OrdersDetailsView(View):
    pass
