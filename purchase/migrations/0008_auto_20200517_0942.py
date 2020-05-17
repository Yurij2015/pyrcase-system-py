# Generated by Django 2.2.12 on 2020-05-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0007_auto_20200517_0929'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'verbose_name': 'Договор на закупку', 'verbose_name_plural': 'Договора на закупку'},
        ),
        migrations.AlterModelOptions(
            name='deal',
            options={'verbose_name': 'Сделка', 'verbose_name_plural': 'Сделки'},
        ),
        migrations.AlterModelOptions(
            name='delivery',
            options={'verbose_name': 'Поставки', 'verbose_name_plural': 'Поставки'},
        ),
        migrations.AlterModelOptions(
            name='purchase',
            options={'verbose_name': 'Закупки', 'verbose_name_plural': 'Закупки'},
        ),
        migrations.AlterModelOptions(
            name='receipt',
            options={'verbose_name': 'Приемки', 'verbose_name_plural': 'Приемки'},
        ),
        migrations.AlterModelOptions(
            name='storehouse',
            options={'verbose_name': 'Склад', 'verbose_name_plural': 'Склады'},
        ),
        migrations.AlterModelOptions(
            name='vendor',
            options={'verbose_name': 'Поставщик', 'verbose_name_plural': 'Поставщики'},
        ),
        migrations.AddField(
            model_name='contract',
            name='document',
            field=models.FileField(help_text='Выберите файл', null=True, upload_to='purchase/uploads'),
        ),
    ]