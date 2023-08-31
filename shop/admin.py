from django.contrib import admin
from shop.models import Category, Product, ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'slug', 'price', 'available', 'availability', 'category', 'is_recommend', 'ordering', 'production_time',
    )
    list_filter = ('available', )
    list_editable = ('price', 'available', 'availability', 'is_recommend', 'ordering', 'production_time')
    prepopulated_fields = {'slug': ('name', )}


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', )
