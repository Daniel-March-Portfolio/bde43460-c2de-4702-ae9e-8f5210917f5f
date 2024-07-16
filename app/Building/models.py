from uuid import UUID, uuid4

from django.db import models


class Building(models.Model):
    uuid: UUID = models.UUIDField(primary_key=True, default=uuid4)
    address: str = models.TextField()

    def __str__(self):
        return f"{self.address}"
