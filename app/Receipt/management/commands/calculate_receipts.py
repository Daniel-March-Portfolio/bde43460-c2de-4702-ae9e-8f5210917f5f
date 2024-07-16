from datetime import date

from django.core.management.base import BaseCommand

from Apartment.models import Apartment
from Receipt.tasks import calculate_receipt_for_apartment_with_celery


class Command(BaseCommand):
    help = "Calculate receipts for all apartments"

    def handle(self, *args, **options):
        current_date = date.today()

        for apartment in Apartment.objects.all():
            calculate_receipt_for_apartment_with_celery.delay(
                apartment_uuid=apartment.uuid,
                month=current_date.month - 1,
                year=current_date.year
            )
