from rest_framework import permissions
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from Progress.models import Progress
from Progress.serializers import ProgressSerializer


class ProgressRetrieve(RetrieveModelMixin, GenericViewSet):
    serializer_class = ProgressSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return Progress.objects.all()
