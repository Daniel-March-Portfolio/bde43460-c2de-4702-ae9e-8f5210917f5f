from rest_framework import serializers

from Apartment.models import Apartment


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ("uuid", "building", "number", "area", "water_tariff", "area_tariff",)
        read_only_fields = ("uuid",)
