from rest_framework import serializers

from Receipt.models import Receipt


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ("uuid", "apartment", "water_payment", "area_payment", "month", "year",)
        read_only_fields = ("uuid", "total_payment",)
