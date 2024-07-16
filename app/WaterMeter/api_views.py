from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from WaterMeter.models import WaterMeter, WaterMeterHistory
from WaterMeter.serializers import WaterMeterSerializer, WaterMeterHistorySerializer


class WaterMeterViewSet(ModelViewSet):
    serializer_class = WaterMeterSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return WaterMeter.objects.all()


class WaterMeterHistoryViewSet(ModelViewSet):
    serializer_class = WaterMeterHistorySerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return WaterMeterHistory.objects.all()
