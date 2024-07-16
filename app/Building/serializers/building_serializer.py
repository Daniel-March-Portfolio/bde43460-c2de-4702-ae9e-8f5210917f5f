from rest_framework import serializers

from Apartment.serializers import ApartmentSerializer
from Building.models import Building


class BuildingSerializer(serializers.ModelSerializer):
    apartments = ApartmentSerializer("apartments",many=True, read_only=True)

    class Meta:
        model = Building
        fields = ("uuid", "address", "apartments", )
        read_only_fields = ("uuid",)
