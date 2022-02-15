from rest_framework import serializers

from garages.models import Garage, GarageType, Indicators, Renter


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
            'phone_number',
            'balance',
        )


class GarageTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = GarageType
        fields = (
            'type',
            'price',
        )


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


class ShortGarageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Garage
        fields = (
            'id',
            'number',
        )


class RenterReadSerializer(RenterCreateAndUpdateSerializer):
    rented_garages = ShortGarageSerializer(
        source='garage', many=True, read_only=True
    )

    class Meta:
        model = Renter
        fields = (
            'id',
            'name',
            'phone_number',
            'rented_garages',
            'balance',
        )
        read_only_fields = ('balance',)


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
            'rent_pay',
            'electricity_price',
            'amount',
            'date',
        )
        read_only_fields = (
            'rent_pay',
            'electricity_price',
            'amount',
            'date',
        )

    def create(self, validated_data):
        return Indicators.objects.create(**validated_data)
