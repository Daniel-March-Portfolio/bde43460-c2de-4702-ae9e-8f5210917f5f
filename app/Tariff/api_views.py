from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from Tariff.models import AreaTariff, WaterTariff
from Tariff.serializers import WaterTariffSerializer, AreaTariffSerializer


class AreaTariffViewSet(ModelViewSet):
    serializer_class = AreaTariffSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return AreaTariff.objects.all()


class WaterTariffViewSet(ModelViewSet):
    serializer_class = WaterTariffSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return WaterTariff.objects.all()
