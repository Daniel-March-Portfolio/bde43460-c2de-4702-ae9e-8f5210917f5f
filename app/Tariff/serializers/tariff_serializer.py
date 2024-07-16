from rest_framework import serializers

from Tariff.models import AreaTariff, WaterTariff


class BaseTariffSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("uuid", "title", "price",)
        read_only_fields = ("uuid",)


class WaterTariffSerializer(BaseTariffSerializer):
    class Meta(BaseTariffSerializer.Meta):
        model = WaterTariff


class AreaTariffSerializer(BaseTariffSerializer):
    class Meta(BaseTariffSerializer.Meta):
        model = AreaTariff
