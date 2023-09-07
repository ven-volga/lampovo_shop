from django.shortcuts import render, redirect
from django.views import View


class OrdersPageView(View):
    template_name = 'sales/orders.html'

    def get(self, request):
        if request.user.is_authenticated and request.user.role in ('AM', 'DEV',):
            return render(request, self.template_name)

        else:
            return redirect('main_page')
