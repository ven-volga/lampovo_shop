from django.shortcuts import render, get_object_or_404
from django.views import View

from cart.forms import CartAddProductForm
from shop.models import Category, Product


class ProductListView(View):
    template_name = 'shop/shop.html'

    def get(self, request, category_slug=None):
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        cart_product_form = CartAddProductForm()

        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)

        context = {
            'category': category,
            'categories': categories,
            'products': products,
            'cart_product_form': cart_product_form,
        }

        return render(request, self.template_name, context)


class ProductDetailView(View):
    template_name = 'shop/details.html'

    def get(self, request, id, slug):
        product = get_object_or_404(Product, id=id, slug=slug, available=True)
        cart_product_form = CartAddProductForm()
        context = {
            'product_detail': product,
            'cart_product_form': cart_product_form,
        }
        return render(request, self.template_name, context)
