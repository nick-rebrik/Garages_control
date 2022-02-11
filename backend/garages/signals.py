from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Indicators


def indicators_calculation(instance, indicator):
    last_indicator = instance.garage.indicators.first
    return (indicator - last_indicator) * instance.garage.tariff


@receiver(pre_save, sender=Indicators)
def pre_save_indicators(created, **kwargs):
    instance = kwargs['instance']
    indicator = instance.indicator
    renter = instance.garage.renter
    if renter:
        if created:
            instance.amount = indicators_calculation(instance, indicator)
            instance.save()
            renter.balance -= instance.amount
            renter.save()
        renter.balance += instance.amount
        renter.save()
        previous_indicator = Indicators.objects.filter(
            garage=instance.garage
        )[-2]
        instance.amount = indicators_calculation(instance, previous_indicator)
        instance.save()
        renter.balance -= instance.amount
        renter.save()
