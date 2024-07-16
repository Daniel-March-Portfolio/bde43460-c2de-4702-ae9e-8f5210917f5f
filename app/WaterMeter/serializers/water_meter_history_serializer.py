from rest_framework import serializers

from WaterMeter.models import WaterMeterHistory


class WaterMeterHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterMeterHistory
        fields = ("uuid", "meter", "value", "month", "year",)
        read_only_fields = ("uuid",)
