from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from garages.models import Garage, GarageType, Renter
from .serializers import (GarageSerializer, GarageTypeSerializer,
                          IndicatorsSerializer,
                          RenterCreateAndUpdateSerializer,
                          RenterReadSerializer)


class GarageViewSet(viewsets.ModelViewSet):
    queryset = Garage.objects.all().select_related('renter', 'type')
    serializer_class = GarageSerializer


class GarageTypeViewSet(viewsets.ModelViewSet):
    queryset = GarageType.objects.all()
    serializer_class = GarageTypeSerializer


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
