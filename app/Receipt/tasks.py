import logging
from uuid import UUID

from celery import shared_task

from Apartment.models import Apartment
from Progress.models import Progress
from Receipt.utils.calculate_receipt import calculate_receipt_for_apartment


@shared_task
def calculate_receipt_for_apartments_with_celery(progress_uuid: UUID, month: int, year: int):
    for apartment in Apartment.objects.all():
        try:
            calculate_receipt_for_apartment(apartment_uuid=apartment.uuid, month=month, year=year)
        except BaseException as e:
            logging.error(f"Failed to calculate receipt for apartment {apartment.uuid}: {e}")
        progress = Progress.objects.get(uuid=progress_uuid)
        progress.value += 1
        progress.save()
