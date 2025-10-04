from django.contrib import admin

from .models import PurchaseHistory, BillingAddress, OrderItem

# Register your models here.
admin.site.register(PurchaseHistory)
admin.site.register(BillingAddress)
admin.site.register(OrderItem)
