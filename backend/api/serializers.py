from rest_framework import serializers

from garages.models import Garage, Renter, Indicators


class RenterCreateAndUpdateSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(
        max_digits=7,
        decimal_places=2,
        default='0.00'
    )

    class Meta:
        model = Renter
        fields = (
            'name',
            'number',
            'balance',
        )


class RenterReadSerializer(RenterCreateAndUpdateSerializer):
    class Meta:
        model = Renter
        fields = (
            'id',
            'name',
            'number',
            'balance',
        )
        read_only_fields = ('balance',)


class GarageSerializer(serializers.ModelSerializer):
    renter = serializers.SlugRelatedField(
        queryset=Renter.objects.all(),
        slug_field='name',
        required=False,
    )

    class Meta:
        model = Garage
        fields = (
            'id',
            'number',
            'renter',
            'tariff',
        )


class IndicatorsSerializer(serializers.ModelSerializer):
    garage = serializers.SlugRelatedField(
        queryset=Garage.objects.all(),
        slug_field='number',
    )

    class Meta:
        model = Indicators
        fields = (
            'id',
            'garage',
            'indicator',
            'amount',
            'date',
        )
        read_only_fields = (
            'amount',
            'date',
        )

    def create(self, validated_data):
        return Indicators.objects.create(**validated_data)
