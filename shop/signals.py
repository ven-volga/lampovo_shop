from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import ProductImage


@receiver(pre_delete, sender=ProductImage)
def delete_image(sender, instance, **kwargs):
    instance.image.delete(False)
