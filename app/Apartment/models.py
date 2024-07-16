from uuid import uuid4, UUID

from django.core.validators import MinValueValidator
from django.db import models

from Building.models import Building
from Tariff.models import WaterTariff, AreaTariff


class Apartment(models.Model):
    uuid: UUID = models.UUIDField(primary_key=True, default=uuid4)

    building: UUID = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="apartments")
    number: str = models.IntegerField(validators=[MinValueValidator(0)])
    area: float = models.FloatField(validators=[MinValueValidator(0)])
    water_tariff: UUID = models.ForeignKey(
        WaterTariff, on_delete=models.SET_NULL, null=True, blank=True, related_name="apartments"
    )
    area_tariff: UUID = models.ForeignKey(
        AreaTariff, on_delete=models.SET_NULL, null=True, blank=True, related_name="apartments"
    )

    class Meta:
        unique_together = ("building", "number",)

    def __str__(self):
        return f"{self.building} : {self.number}"
