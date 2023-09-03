from django.shortcuts import render, redirect
from django.views import View
from cart.cart import Cart
from lampovo_shop import settings
from orders.forms import OrderAddForm
from orders.models import Order, OrderItem
from orders.utils import send_order_email
from shop.models import Product


class CheckoutView(View):
    template_name = 'shop/checkout.html'
    login_redirect = 'login'
    complete_template = 'shop/complete.html'

    @staticmethod
    def get_cart_products(request):
        cart = Cart(request)
        total_price = cart.get_total_price()
        cart = request.session.get(settings.CART_SESSION_ID)
        cart_items = cart
        cart_products = []

        for product_id, item_data in cart_items.items():
            product = Product.objects.get(id=product_id)
            quantity = item_data['quantity']
            price = product.price
            total_item_price = price * quantity
            main_image = product.main_image
            url = Product.get_absolute_url(product)

            cart_products.append({
                'name': product,
                'quantity': quantity,
                'price': price,
                'total_item_price': total_item_price,
                'main_image': main_image,
                'url': url,
            })

        context = {
            'client_cart': cart,
            'cart_products': cart_products,
            'total_price': total_price,
            'order_form': OrderAddForm(),
        }

        return context

    def get(self, request):
        cart = Cart(request)

        if not cart:
            context = {
                'message': 'You have no items in cart'
            }
            return render(request, self.template_name, context)

        elif request.user.is_authenticated and cart:
            context = self.get_cart_products(request)
            order_form = OrderAddForm()
            context['order_form'] = order_form
            return render(request, self.template_name, context)

        else:
            return redirect(self.login_redirect)

    def post(self, request):
        order_form = OrderAddForm(request.POST)
        if order_form.is_valid():
            cart = Cart(request)
            order = Order(
                customer=request.user,
                total_price=cart.get_total_price(),
                comment=order_form.cleaned_data['comment'],
            )
            order.save()

            user = request.user

            user.first_name = order_form.cleaned_data['first_name']
            user.last_name = order_form.cleaned_data['last_name']
            user.phone_number = order_form.cleaned_data['phone_number']
            user.country = order_form.cleaned_data['country']
            user.city = order_form.cleaned_data['city']
            user.zip = order_form.cleaned_data['zip']
            user.address = order_form.cleaned_data['address']

            user.save()

            cart = request.session.get(settings.CART_SESSION_ID)

            for product_id, item_data in cart.items():
                product = Product.objects.get(id=product_id)
                quantity = item_data['quantity']
                price = product.price * quantity
                order_item = OrderItem(order=order, product=product, quantity=quantity, subtotal_price=price)
                order_item.save()

            cart.clear()

            send_order_email(request, request.user)

            return render(request, self.complete_template)

        else:
            context = self.get_cart_products(request)
            context.update({'order_form': order_form})
            return render(request, self.template_name, context)


class CompleteView(View):
    template_name = 'shop/complete.html'

    def get(self, request):
        context = {
        }
        return render(request, self.template_name, context)
