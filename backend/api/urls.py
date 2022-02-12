from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import GarageViewSet, RenterViewSet, IndicatorsViewSet

app_name = 'api'

router = DefaultRouter()
router.register('garages', GarageViewSet, basename='garages')
router.register('renters', RenterViewSet, basename='renters')
router.register(
    'garages/(?P<garage_id>[0-9]+)/indicators',
    IndicatorsViewSet,
    basename='indicators'
)

urlpatterns = [
    path('', include(router.urls))
]