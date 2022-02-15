from datetime import datetime

from django.db import models


class Garage(models.Model):
    number = models.IntegerField('Номер гаражу', unique=True)
    renter = models.ForeignKey(
        'Renter',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Орендар',
        related_name='garage'
    )
    type = models.ForeignKey(
        'GarageType',
        on_delete=models.PROTECT,
        verbose_name='Тип гаражу',
        related_name='garage'
    )
    tariff = models.DecimalField(
        'Тариф за електроенергію',
        max_digits=7,
        decimal_places=2,
    )

    class Meta:
        ordering = ('number',)
        verbose_name = 'Гараж'
        verbose_name_plural = 'Гаражі'

    def __str__(self):
        return f'{self.number}'


class GarageType(models.Model):
    type = models.CharField('Тип гаража', max_length=125)
    price = models.DecimalField(
        'Орендна плата',
        max_digits=7,
        decimal_places=2
    )

    class Meta:
        verbose_name = 'Тип гаражу'
        verbose_name_plural = 'Типи гаражів'

    def __str__(self):
        return f'{self.type} - {self.price} грн.'


class Renter(models.Model):
    name = models.CharField('Ім\'я та Фамілія', max_length=250)
    phone_number = models.CharField(
        'Номер телефону',
        max_length=11,
        unique=True
    )
    balance = models.DecimalField(
        'Баланс',
        max_digits=7,
        decimal_places=2,
        default='0.00',
        null=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Орендар'
        verbose_name_plural = 'Орендарі'

    def __str__(self):
        return f'{self.name}'


class Indicators(models.Model):
    indicator = models.IntegerField('Показник лічильника')
    garage = models.ForeignKey(
        Garage,
        on_delete=models.CASCADE,
        verbose_name='Гараж',
        related_name='indicators'
    )
    rent_pay = models.DecimalField(
        'Орендна плата',
        max_digits=7,
        decimal_places=2,
        default='0.00',
        blank=True,
        null=True,
    )
    electricity_price = models.DecimalField(
        'Плата за електроенергію',
        max_digits=7,
        decimal_places=2,
        default='0.00',
        blank=True,
        null=True,
    )
    amount = models.DecimalField(
        'Сумма до оплати',
        max_digits=7,
        decimal_places=2,
        default='0.00',
        blank=True,
        null=True,
    )
    date = models.DateTimeField('Дата', auto_now_add=True)

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Показник лічильника'
        verbose_name_plural = 'Показники лічильника'

    def __str__(self):
        return f'Гараж №{self.garage}. {datetime.date(self.date)}'
