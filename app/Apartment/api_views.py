from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from Apartment.models import Apartment
from Apartment.serializers import ApartmentSerializer


class ApartmentViewSet(ModelViewSet):
    serializer_class = ApartmentSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return Apartment.objects.all()
