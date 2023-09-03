from django.db import models
from authentication.models import User
from shop.models import Product


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('NEW', 'New order'),
        ('WFP', 'Waiting for payment'),
        ('IP', 'In production'),
        ('CMP', 'Completing'),
        ('SHP', 'Shipped'),
    ]

    order_id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    order_status = models.CharField(max_length=4, choices=ORDER_STATUS_CHOICES, default='NEW')
    comment = models.TextField(max_length=1000, blank=True, null=True)
    # promo_code = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        ordering = ('order_id',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return str(self.order_id)

    def get_total_price(self):
        return sum(item.total_price() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal_price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_price(self):
        return self.quantity * self.price
