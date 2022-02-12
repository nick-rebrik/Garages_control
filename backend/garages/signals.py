from decimal import Decimal

from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

from .models import Indicators


def indicators_calculation(instance, indicator, update=None):
    if update is None:
        last_indicator = instance.garage.indicators.first().indicator
    else:
        last_indicator = instance.garage.indicators.all()[1].indicator
    return Decimal((indicator - last_indicator) * instance.garage.tariff)


@receiver(pre_save, sender=Indicators)
def pre_save_indicators(instance, **kwargs):
    indicator = instance.indicator
    renter = instance.garage.renter
    if renter and instance.garage.indicators.exists():
        if instance.pk is None:
            instance.amount = indicators_calculation(instance, indicator)
            renter.balance -= instance.amount
        else:
            renter.balance += instance.amount
            instance.amount = indicators_calculation(instance, indicator, True)
            renter.balance -= instance.amount
    renter.save()


@receiver(pre_delete, sender=Indicators)
def pre_delete_indicators(instance, **kwargs):
    renter = instance.garage.renter
    if renter:
        renter.balance += instance.amount or 0
        renter.save()
