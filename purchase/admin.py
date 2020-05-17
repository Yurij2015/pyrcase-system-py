from django.contrib import admin
from .models import Purchase, Deal, Contract, Delivery, Receipt, Storehouse, Vendor


# Register your models here.

# admin.site.register(Purchase)

def contract(obj):
    return obj.contract.all().count()


def purchase(obj):
    return obj.purchase.all().count()


def delivery(obj):
    return obj.delivery.all().count()


def storehouse(obj):
    return obj.storehouse.all().count()


admin.site.site_header = 'Поддержка электронных закупок'


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'date', 'contract')


admin.site.register(Purchase, PurchaseAdmin)


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('number', 'document')


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'date', 'purchase')


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'date', 'delivery', 'storehouse')


@admin.register(Storehouse)
class StorehouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', 'address')


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', 'address')

# admin.site.register(Deal)
# admin.site.register(Contract)
# admin.site.register(Delivery)
# admin.site.register(Receipt)
# admin.site.register(Storehouse)
# admin.site.register(Vendor)
