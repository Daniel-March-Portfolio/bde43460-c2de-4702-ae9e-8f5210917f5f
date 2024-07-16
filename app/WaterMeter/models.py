from uuid import UUID, uuid4

from django.core.validators import MinValueValidator
from django.db import models

from Apartment.models import Apartment
from Main.constants import MONTHS_CHOICES, MIN_YEAR


class WaterMeter(models.Model):
    uuid: UUID = models.UUIDField(primary_key=True, default=uuid4)
    mark: str = models.TextField(blank=True, null=False)
    apartment: UUID = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name="water_meters")

    def __str__(self):
        return f"{self.apartment} ({self.uuid})"


class WaterMeterHistory(models.Model):
    uuid: UUID = models.UUIDField(primary_key=True, default=uuid4)
    meter: UUID = models.ForeignKey(WaterMeter, on_delete=models.CASCADE, related_name="history")
    value: int = models.IntegerField(validators=[MinValueValidator(0)])
    month: int = models.IntegerField(choices=MONTHS_CHOICES)
    year: int = models.IntegerField(validators=[MinValueValidator(MIN_YEAR)])

    class Meta:
        verbose_name_plural = "Water meter histories"
        unique_together = ("meter", "month", "year",)

    def __str__(self):
        return f"{self.meter} : {self.month} {self.year}"
