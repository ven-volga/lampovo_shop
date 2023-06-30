from django.contrib import admin
from .models import *


class SubscriberAdmin(admin.ModelAdmin):
    # list_display = ['email', 'name']
    list_display = [field.name for field in Subscriber._meta.fields]
    # exclude = ['name']

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)
