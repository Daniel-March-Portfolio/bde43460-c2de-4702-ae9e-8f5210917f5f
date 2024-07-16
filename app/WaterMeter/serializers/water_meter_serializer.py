from rest_framework import serializers

from WaterMeter.models import WaterMeter


class WaterMeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterMeter
        fields = ("uuid", "mark", "apartment",)
        read_only_fields = ("uuid",)
