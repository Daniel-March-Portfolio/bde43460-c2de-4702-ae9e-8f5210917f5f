from rest_framework import serializers

from Building.models import Building


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ("uuid", "address", )
        read_only_fields = ("uuid",)
