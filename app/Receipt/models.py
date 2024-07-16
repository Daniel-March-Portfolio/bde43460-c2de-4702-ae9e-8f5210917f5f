from uuid import uuid4, UUID

from django.core.validators import MinValueValidator
from django.db import models

from Apartment.models import Apartment
from Main.constants import MONTHS_CHOICES, MIN_YEAR


class Receipt(models.Model):
    uuid: UUID = models.UUIDField(primary_key=True, default=uuid4)
    apartment: UUID = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name="receipts")
    water_payment: int = models.IntegerField(validators=[MinValueValidator(0)])
    area_payment: int = models.IntegerField(validators=[MinValueValidator(0)])
    month: int = models.IntegerField(choices=MONTHS_CHOICES)
    year: int = models.IntegerField(validators=[MinValueValidator(MIN_YEAR)])

    @property
    def total_payment(self):
        return self.water_payment + self.area_payment

    def __str__(self):
        return f"{self.apartment} : {self.month} {self.year}"

    class Meta:
        unique_together = ("apartment", "month", "year",)
