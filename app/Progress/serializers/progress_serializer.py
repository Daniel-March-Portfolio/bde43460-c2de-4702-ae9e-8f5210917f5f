from rest_framework import serializers

from Progress.models import Progress


class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ("uuid", "percentage",)
        read_only_fields = ("uuid", "percentage",)
