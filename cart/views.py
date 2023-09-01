from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


class CartView(View):
    template_name = 'cart/summary.html'

    def get(self, request):
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                       'update': True})
        context = {
            'cart': cart
        }
        return render(request, self.template_name, context)

    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)

        quantity = request.POST.get('quantity')

        if quantity:
            if form.is_valid():
                cd = form.cleaned_data
                cart.add(product=product,
                         quantity=cd['quantity'],
                         update_quantity=cd['update'])
        else:
            cart.remove(product)

        return redirect('cart:cart_detail')
