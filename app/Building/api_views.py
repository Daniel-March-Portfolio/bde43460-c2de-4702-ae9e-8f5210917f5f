from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from Building.models import Building
from Building.serializers import BuildingSerializer


class BuildingViewSet(ModelViewSet):
    serializer_class = BuildingSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return Building.objects.all()
