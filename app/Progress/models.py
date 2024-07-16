from uuid import UUID, uuid4

from django.core.validators import MinValueValidator
from django.db import models


class Progress(models.Model):
    uuid: UUID = models.UUIDField(primary_key=True, default=uuid4)
    value: int = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    target_value: int = models.IntegerField(validators=[MinValueValidator(1)])

    @property
    def percentage(self):
        return min(100 * (self.value / self.target_value), 100.).__round__(2)
