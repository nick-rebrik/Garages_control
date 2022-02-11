from django.contrib import admin

from .models import Garage, Renter, Indicators


@admin.register(Garage)
class GarageAdmin(admin.ModelAdmin):
    fields = (
        'number',
        'renter',
        'tariff',
    )
    search_fields = ('number',)


@admin.register(Renter)
class RenterAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'number',
        'balance',
    )
    search_fields = ('name',)
    list_display = ('name', 'balance')


@admin.register(Indicators)
class IndicatorsAdmin(admin.ModelAdmin):
    fields = (
        'indicator',
        'garage',
        'amount',
        'date',
    )
    search_fields = ('garage',)
    list_display = ('garage', 'indicator', 'amount', 'date')
