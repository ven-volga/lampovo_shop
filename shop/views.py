from django.shortcuts import render, get_object_or_404
from django.views import View

from shop.models import Category, Product


class ProductListView(View):
    template_name = 'shop/main.html'

    def get(self, request, category_slug=None):
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)

        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)

        context = {
            'category': category,
            'categories': categories,
            'products': products,
        }

        return render(request, self.template_name, context)


class ProductDetailView(View):
    template_name = 'shop/details.html'

    def get(self, request, id, slug):
        product = get_object_or_404(Product, id=id, slug=slug, available=True)
        context = {
            'product_detail': product,
        }
        return render(request, self.template_name, context)
