from uuid import UUID

from django.db.models import Q

from Apartment.models import Apartment
from Receipt.models import Receipt
from WaterMeter.models import WaterMeterHistory


def calculate_receipt_for_apartment(*, apartment_uuid: UUID, month: int, year: int):
    apartment = Apartment.objects.get(uuid=apartment_uuid)
    Receipt.objects.filter(apartment=apartment, month=month, year=year).delete()

    area_payment = 0
    water_payment = 0
    if apartment.area_tariff is not None:
        area_payment = apartment.area_tariff.price * apartment.area
    if apartment.water_tariff is not None:
        for water_meter in apartment.water_meters.all():
            prev_water_meter_value = get_prev_water_meter_value(
                water_meter_uuid=water_meter.uuid, month=month, year=year
            )
            water_meter_value = get_water_meter_value(
                water_meter_uuid=water_meter.uuid, month=month, year=year
            )
            water_payment += max(0, water_meter_value - prev_water_meter_value) * apartment.water_tariff.price

    Receipt.objects.create(
        apartment=apartment,
        month=month,
        year=year,
        water_payment=water_payment,
        area_payment=area_payment
    )


def get_prev_water_meter_value(water_meter_uuid: UUID, month: int, year: int):
    prev_water_meter_history = (
        WaterMeterHistory.objects
        .filter(Q(year__lt=year) | Q(year=year, month__lt=month), meter__uuid=water_meter_uuid)
        .order_by("-year", "-month")
        .first()
    )
    return prev_water_meter_history.value if prev_water_meter_history is not None else 0


def get_water_meter_value(water_meter_uuid: UUID, month: int, year: int):
    water_meter_history = (
        WaterMeterHistory.objects
        .filter(meter__uuid=water_meter_uuid, year=year, month=month)
        .first()
    )
    return water_meter_history.value if water_meter_history is not None else 0
