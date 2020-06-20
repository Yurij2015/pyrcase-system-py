from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PurchaseConfig(AppConfig):
    name = 'purchase'
    # verbose_name = "Закупки"
    verbose_name = _('Закупки')
