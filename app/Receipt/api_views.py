from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from Receipt.models import Receipt
from Receipt.serializers import ReceiptSerializer


class ReceiptViewSet(ModelViewSet):
    serializer_class = ReceiptSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return Receipt.objects.all()
