from django.shortcuts import render
from django.views import generic

# Create your views here.
from .models import Purchase, Vendor, Deal, Delivery, Receipt, Storehouse, Contract


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_purchases = Purchase.objects.all().count()
    num_vendor = Vendor.objects.all().count()
    num_deal = Deal.objects.all().count()
    num_delivery = Delivery.objects.all().count()
    num_receipt = Receipt.objects.all().count()
    num_storehouse = Storehouse.objects.all().count()
    num_contract = Contract.objects.all().count()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_purchases': num_purchases, 'num_vendor': num_vendor,
                 'num_deal': num_deal, 'num_delivery': num_delivery, 'num_receipt': num_receipt,
                 'num_storehouse': num_storehouse, 'num_contract': num_contract},
    )


class PurchaseListView(generic.ListView):
    model = Purchase
