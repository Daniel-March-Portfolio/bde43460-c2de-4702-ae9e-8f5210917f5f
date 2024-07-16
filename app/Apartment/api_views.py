from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions
from rest_framework.viewsets import ModelViewSet

from Apartment.models import Apartment
from Apartment.serializers import ApartmentSerializer


class ApartmentViewSet(ModelViewSet):
    serializer_class = ApartmentSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend,)
    filterset_fields = ("building", "number", "area", "area", "area", "water_tariff", "area_tariff",)

    def get_queryset(self):
        return Apartment.objects.all()
