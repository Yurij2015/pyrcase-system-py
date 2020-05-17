from django.contrib import admin
from .models import Purchase, Deal, Contract, Delivery, Receipt, Storehouse, Vendor
# Register your models here.

admin.site.register(Purchase)
admin.site.register(Deal)
admin.site.register(Contract)
admin.site.register(Delivery)
admin.site.register(Receipt)
admin.site.register(Storehouse)
admin.site.register(Vendor)
