from django.shortcuts import render
from django.views import View
from cart.cart import Cart
from lampovo_shop import settings
from orders.forms import OrderAddForm
from orders.models import Order, OrderItem
from shop.models import Product


class CheckoutView(View):
    template_name = 'shop/checkout.html'
    template_redirect = 'registration/login.html'

    def get(self, request):
        if request.user.is_authenticated:
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

                cart_products.append({
                    'name': product,
                    'quantity': quantity,
                    'price': price,
                    'total_item_price': total_item_price,
                    'main_image': main_image,
                })

            context = {
                'cart': cart,
                'cart_products': cart_products,
                'total_price': total_price,
                'order_form': OrderAddForm(),
            }

            return render(request, self.template_name, context)
        else:
            return render(request, self.template_redirect)

    def post(self, request):
        order_form = OrderAddForm(request.POST)
        if order_form.is_valid():
            cart = Cart(request)
            order = Order(
                customer=request.user,
                total_price=cart.get_total_price(),
                shipping=request.POST.get('shipping'))
            order.save()

            cart = request.session.get(settings.CART_SESSION_ID)

            for product_id, item_data in cart.items():
                product = Product.objects.get(id=product_id)
                quantity = item_data['quantity']
                price = product.price * quantity
                order_item = OrderItem(order=order, product=product, quantity=quantity, subtotal_price=price)
                order_item.save()

            cart.clear()

        context = {'order_form': order_form}
        return render(request, self.template_name, context)
