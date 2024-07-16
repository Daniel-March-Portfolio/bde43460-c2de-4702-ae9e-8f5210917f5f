from datetime import date
from uuid import UUID

from celery import shared_task
from django.core.management.base import BaseCommand

from Apartment.models import Apartment
from Progress.models import Progress
from Receipt.tasks import calculate_receipt_for_apartments_with_celery


class Command(BaseCommand):
    help = "Calculate receipts for all apartments"

    def handle(self, *args, progress_uuid: UUID = None, **options):
        current_date = date.today()
        if progress_uuid is None:
            progress_uuid = Progress.objects.create(
                target_value=Apartment.objects.count()
            ).uuid
        else:
            Progress.objects.filter(uuid=progress_uuid).update(target_value=Apartment.objects.count())
        calculate_receipt_for_apartments_with_celery.delay(
            progress_uuid=progress_uuid, month=current_date.month - 1, year=current_date.year
        )

