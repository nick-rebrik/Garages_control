from django.db import models


class Garage(models.Model):
    numebr = models.IntegerField('Номер гаражу')
    renter = models.ForeignKey(
        'Renter',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Орендар',
        related_name='garage'
    )
    tariff = models.DecimalField('Тариф')

    class Meta:
        ordering = ('numebr',)
        verbose_name = 'Гараж'
        verbose_name_plural = 'Гаражи'

    def __str__(self):
        return f'{self.numebr}'


class Renter(models.Model):
    name = models.CharField('Ім\'я Фамілія', max_length=250)
    number = models.IntegerField('Номер телефону')
    balance = models.DecimalField('Баланс')

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
    amount = models.DecimalField('Сумма до оплати', blank=True, null=True)
    date = models.DateTimeField('Дата', auto_now_add=True)

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Показник лічильника'
        verbose_name_plural = 'Показники лічильника'
