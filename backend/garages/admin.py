from django.contrib import admin

from .models import Garage, Indicators, Renter


@admin.register(Garage)
class GarageAdmin(admin.ModelAdmin):
    fields = (
        'number',
        'renter',
        'tariff',
    )
    search_fields = ('number',)
    list_display = ('number', 'renter')


@admin.register(Renter)
class RenterAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'phone_number',
        'balance',
    )
    search_fields = ('name',)
    list_display = ('name', 'balance')


@admin.register(Indicators)
class IndicatorsAdmin(admin.ModelAdmin):
    fields = (
        'garage',
        'indicator',
        'amount',
    )
    search_fields = ('garage',)
    list_display = ('garage', 'indicator', 'amount', 'date')
