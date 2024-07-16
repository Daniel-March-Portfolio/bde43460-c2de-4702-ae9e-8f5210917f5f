from uuid import UUID

from celery import shared_task

from Receipt.utils.calculate_receipt import calculate_receipt_for_apartment


@shared_task
def calculate_receipt_for_apartment_with_celery(apartment_uuid: UUID, month: int, year: int):
    calculate_receipt_for_apartment(apartment_uuid=apartment_uuid, month=month, year=year)
