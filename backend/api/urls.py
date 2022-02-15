from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (GarageTypeViewSet, GarageViewSet, RenterViewSet,
                    IndicatorsViewSet, PaymentViewSet)

app_name = 'api'

router = DefaultRouter()
router.register('garages', GarageViewSet, basename='garages')
router.register('garages_type', GarageTypeViewSet, basename='garages_type')
router.register('renters', RenterViewSet, basename='renters')
router.register(
    'garages/(?P<garage_id>[0-9]+)/indicators',
    IndicatorsViewSet,
    basename='indicators'
)
router.register('payments', PaymentViewSet, basename='payments')

urlpatterns = [
    path('', include(router.urls))
]