from rest_framework import viewsets

from garages.models import Garage, Renter
from rest_framework.generics import get_object_or_404

from .serializers import (GarageSerializer, IndicatorsSerializer,
                          RenterCreateAndUpdateSerializer,
                          RenterReadSerializer)


class GarageViewSet(viewsets.ModelViewSet):
    queryset = Garage.objects.all().select_related('renter')
    serializer_class = GarageSerializer


class RenterViewSet(viewsets.ModelViewSet):
    queryset = Renter.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return RenterReadSerializer
        return RenterCreateAndUpdateSerializer


class IndicatorsViewSet(viewsets.ModelViewSet):
    serializer_class = IndicatorsSerializer

    def get_queryset(self):
        garage = get_object_or_404(Garage, id=self.kwargs['garage_id'])
        return garage.indicators.all()
