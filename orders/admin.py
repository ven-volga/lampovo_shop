from django.contrib import admin
from orders.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_id', 'created', 'customer', 'total_price',
        'order_items', 'order_status',
    )
    list_filter = ('created', 'customer',)

    def order_items(self, obj):
        items = OrderItem.objects.filter(order=obj)
        item_names = ', '.join([str(item.product) for item in items])
        return item_names

    order_items.short_description = 'Order Items'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'order', 'product', 'quantity', 'subtotal_price',
    )
