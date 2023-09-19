from django.db import models
from authentication.models import User
from shop.models import Product


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('NEW', 'New order'),
        ('WFP', 'Waiting for payment'),
        ('IP', 'In production'),
        ('SHP', 'Shipped'),
        ('CMP', 'Complete'),
    ]

    order_id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    order_status = models.CharField(max_length=4, choices=ORDER_STATUS_CHOICES, default='NEW')
    comment = models.TextField(max_length=1000, blank=True, null=True)
    # promo_code = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        ordering = ('-order_id',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return str(self.order_id)

    def get_total_price(self):
        return sum(item.total_price() for item in self.items.all())

    def get_status_display(self):
        return dict(Order.ORDER_STATUS_CHOICES)[self.order_status]

    def formatted_datetime(self):
        return self.created.strftime("%d %b %Y | %H:%M")

    @staticmethod
    def get_order_info(user_id):
        user_orders = Order.objects.filter(customer_id=user_id)
        order_data = []

        for order in user_orders:
            order_id = order.order_id
            created = order.created
            customer = order.customer
            total_price = order.total_price
            order_status = order.get_status_display()

            order_items = []
            for item in OrderItem.objects.filter(order=order.order_id):
                product = item.product
                quantity = item.quantity
                subtotal_price = item.subtotal_price

                order_items.append({
                    'product': product,
                    'quantity': quantity,
                    'subtotal_price': subtotal_price,
                })

            order_data.append({
                'id': order_id,
                'created': created,
                'customer': customer,
                'total_price': total_price,
                'order_status': order_status,
                'order_items': order_items,
            })

        return order_data


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal_price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_price(self):
        return self.quantity * self.price
