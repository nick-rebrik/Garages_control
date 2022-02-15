from django.contrib import admin

from .models import Garage, GarageType, Indicators, Payment, Renter


@admin.register(Garage)
class GarageAdmin(admin.ModelAdmin):
    fields = (
        'number',
        'renter',
        'type',
        'tariff',
    )
    search_fields = ('number',)
    list_display = ('number', 'renter')


@admin.register(GarageType)
class GarageAdmin(admin.ModelAdmin):
    fields = (
        'type',
        'price',
    )
    list_display = ('type', 'price')


@admin.register(Renter)
class RenterAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'phone_number',
        'rented_garages',
        'balance',
    )
    readonly_fields = ('rented_garages',)
    search_fields = ('name',)
    list_display = ('name', 'balance')

    def rented_garages(self, renter_object):
        garage = renter_object.garage.all()
        return ', '.join((str(item.number) for item in garage))


@admin.register(Indicators)
class IndicatorsAdmin(admin.ModelAdmin):
    fields = (
        'garage',
        'indicator',
        'rent_pay',
        'electricity_price',
        'amount',
    )
    readonly_fields = ('rent_pay', 'electricity_price', 'amount')
    search_fields = ('garage',)
    list_display = ('garage', 'indicator', 'amount', 'date')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    fields = (
        'renter',
        'amount',
        'date'
    )
    readonly_fields = ('date',)
    list_display = ('renter', 'amount', 'date')
    search_fields = ('renter',)
