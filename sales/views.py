from django.shortcuts import render, redirect
from django.views import View

from authentication.models import User
from orders.models import Order, OrderItem
from sales.forms import OrderFilterForm, ChangeStatusForm


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


class OrderDetailsView(View):
    template_name = 'sales/order_details.html'

    def get(self, request, order_id):
        order = Order.objects.get(order_id=order_id)
        order_items = OrderItem.objects.filter(order=order_id)
        ship_info = User.objects.get(email=order.customer)
        form = ChangeStatusForm()

        context = {
            'order': order,
            'order_items': order_items,
            'ship_info': ship_info,
            'form': form,
        }

        if request.user.is_authenticated and request.user.role not in ('CU',):
            return render(request, self.template_name, context)

        return redirect('main_page')

    def post(self, request, order_id):
        form = ChangeStatusForm(request.POST)

        if form.is_valid():
            order = Order.objects.get(order_id=order_id)
            order.order_status = form.cleaned_data['order_status']
            order.save()

            return render(request, self.template_name)

        context = {
            'form': form,
        }

        return render(request, self.template_name, context)
