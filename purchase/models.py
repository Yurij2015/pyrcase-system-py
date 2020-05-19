from django.db import models
from django.urls import reverse


class Deal(models.Model):
    """
    Model representing a deal (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField('Номер сделки', max_length=200, help_text="Введите номер сделки (может включать буквы, "
                                                                      "цифры и другие знаки)")
    date = models.DateField('Дата сделки', help_text="Введите дату сделки")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

    class Meta:
        verbose_name = "Сделка"
        verbose_name_plural = "Сделки"


class Vendor(models.Model):
    title = models.CharField('Наименование поставщика', max_length=50, help_text="Введите наименование поставщика")
    phone = models.CharField('Номер телефона', max_length=18, help_text="Введите номер телефона поставщика")
    address = models.TextField('Адрес поставищка', max_length=200, help_text="Введите адрес поставщика")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.title

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"


class Storehouse(models.Model):
    title = models.CharField('Наименование склада', max_length=50, help_text="Введите наименование склада")
    phone = models.CharField('Номер телефона', max_length=18, help_text="Введите номер телефона склада")
    address = models.TextField('Адрес склада', max_length=200, help_text="Введите адрес склада")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.title

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"


class Contract(models.Model):
    number = models.CharField('Номер договора', max_length=20, help_text="Введите номер договора")
    document = models.FileField(help_text="Выберите файл", upload_to='uploads/', null=True, verbose_name="Ссылка на "
                                                                                                         "документ")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.number

    class Meta:
        verbose_name = "Договор на закупку"
        verbose_name_plural = "Договора на закупку"


class Purchase(models.Model):
    title = models.CharField('Наименование закупки', max_length=200)
    number = models.CharField('Номер закупки', max_length=20, help_text="Введите номер закупки")
    date = models.DateField('Дата закупки', help_text="Введите дату осуществления закупки")
    deal = models.ManyToManyField('Deal', help_text="Выберите номер сделки")
    vendor = models.ManyToManyField('Vendor', help_text="Выберите поставщика")
    contract = models.ForeignKey('Contract', on_delete=models.SET_NULL, null=True, verbose_name="Договор")

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular purchase instance.
        """
        return reverse('purchase-detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Закупки"
        verbose_name_plural = "Закупки"


class Delivery(models.Model):
    """
    Model representing an delivery.
    """
    name = models.CharField('Наименование поставки', max_length=100)
    number = models.CharField('Номер поставки', max_length=100)
    date = models.DateField('Дата поставки', null=True, blank=True)
    purchase = models.ForeignKey('Purchase', on_delete=models.SET_NULL, null=True, verbose_name="Закупки")

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('delivery-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.name, self.number)

    class Meta:
        verbose_name = "Поставки"
        verbose_name_plural = "Поставки"


class Receipt(models.Model):
    """
    Model representing an delivery.
    """
    name = models.CharField('Наименование приемки', max_length=100)
    number = models.CharField('Номер приемки', max_length=100)
    date = models.DateField('Дата поставки', null=True, blank=True)
    delivery = models.ForeignKey('Delivery', on_delete=models.SET_NULL, null=True, help_text="Выберите номер поставки",
                                 verbose_name="Поставки")
    storehouse = models.ForeignKey('Storehouse', on_delete=models.SET_NULL, null=True, help_text="Выберите склад",
                                   verbose_name="Склады")

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('receipt-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.name, self.number)

    class Meta:
        verbose_name = "Приемки"
        verbose_name_plural = "Приемки"
