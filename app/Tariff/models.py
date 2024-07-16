from uuid import UUID, uuid4

from django.core.validators import MinValueValidator
from django.db import models


class _BaseTariff(models.Model):
    uuid: UUID = models.UUIDField(primary_key=True, default=uuid4)
    title: str = models.CharField(max_length=255)
    price: int = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.title}"


class WaterTariff(_BaseTariff):
    pass


class AreaTariff(_BaseTariff):
    pass
