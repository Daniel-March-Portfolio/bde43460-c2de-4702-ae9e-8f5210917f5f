import pytest
from django.test import Client

from Apartment.models import Apartment
from Building.models import Building
from WaterMeter.models import WaterMeter, WaterMeterHistory
from tests.utils.authenticate_user import authenticate_user
from tests.utils.authentication_credentials import ADMIN_AUTHENTICATION_CREDENTIALS
from tests.utils.request import make_get_request_with_json_response, make_post_request_with_json_response, \
    make_delete_request_with_json_response, make_put_request_with_json_response


@pytest.mark.django_db
def test_retrieve(client: Client):
    authenticate_user(client, ADMIN_AUTHENTICATION_CREDENTIALS)

    building = Building.objects.create(address="address")
    apartment = Apartment.objects.create(
        building=building,
        number=1,
        area=100.1,
        water_tariff=None,
        area_tariff=None
    )
    water_meter = WaterMeter.objects.create(
        mark="Some mark",
        apartment=apartment
    )
    water_meter_history = WaterMeterHistory.objects.create(
        meter=water_meter,
        value=10,
        month=1,
        year=2024
    )

    response = make_get_request_with_json_response(client, f"/api/water_meters/history/{water_meter_history.uuid}/")
    assert response.status_code == 200, response.data
    expected_response_data = {
        "uuid": str(water_meter_history.uuid),
        "meter": str(water_meter.uuid),
        "value": 10,
        "month": 1,
        "year": 2024
    }
    assert response.data == expected_response_data, response.data


@pytest.mark.django_db
def test_list(client: Client):
    authenticate_user(client, ADMIN_AUTHENTICATION_CREDENTIALS)

    building = Building.objects.create(address="address")
    apartment = Apartment.objects.create(
        building=building,
        number=1,
        area=100.1,
        water_tariff=None,
        area_tariff=None
    )

    water_meter = WaterMeter.objects.create(
        mark="Some mark",
        apartment=apartment
    )
    water_meter_history_1 = WaterMeterHistory.objects.create(
        meter=water_meter,
        value=10,
        month=1,
        year=2024
    )
    water_meter_history_2 = WaterMeterHistory.objects.create(
        meter=water_meter,
        value=12,
        month=2,
        year=2024
    )

    response = make_get_request_with_json_response(client, f"/api/water_meters/history/")
    assert response.status_code == 200, response.data
    water_meter_history_1_data = {
        "uuid": str(water_meter_history_1.uuid),
        "meter": str(water_meter.uuid),
        "value": 10,
        "month": 1,
        "year": 2024
    }
    water_meter_history_2_data = {
        "uuid": str(water_meter_history_2.uuid),
        "meter": str(water_meter.uuid),
        "value": 12,
        "month": 2,
        "year": 2024
    }
    expected_response_data = sorted([water_meter_history_1_data, water_meter_history_2_data], key=lambda x: x["uuid"])
    got_response_data = sorted(response.data, key=lambda x: x["uuid"])
    assert got_response_data == expected_response_data, response.data


@pytest.mark.django_db
def test_create(client: Client):
    authenticate_user(client, ADMIN_AUTHENTICATION_CREDENTIALS)

    building = Building.objects.create(address="address")
    apartment = Apartment.objects.create(
        building=building,
        number=1,
        area=100.1,
        water_tariff=None,
        area_tariff=None
    )
    water_meter = WaterMeter.objects.create(
        mark="Some mark",
        apartment=apartment
    )
    water_meter_history_data = {
        "meter": str(water_meter.uuid),
        "value": 12,
        "month": 2,
        "year": 2024
    }
    response = make_post_request_with_json_response(client, f"/api/water_meters/history/", data=water_meter_history_data)
    assert response.status_code == 201, response.data
    expected_response_data = {
        "uuid": str(WaterMeterHistory.objects.first().uuid),
        **water_meter_history_data
    }
    assert response.data == expected_response_data, response.data


@pytest.mark.django_db
def test_update(client: Client):
    authenticate_user(client, ADMIN_AUTHENTICATION_CREDENTIALS)

    building = Building.objects.create(address="address")
    apartment = Apartment.objects.create(
        building=building,
        number=1,
        area=100,
        water_tariff=None,
        area_tariff=None
    )
    water_meter = WaterMeter.objects.create(
        mark="Some mark",
        apartment=apartment
    )
    new_water_meter = WaterMeter.objects.create(
        mark="Some mark",
        apartment=apartment
    )
    water_meter_history = WaterMeterHistory.objects.create(
        meter=water_meter,
        value=10,
        month=1,
        year=2024
    )
    water_meter_history_new_data = {
        "meter": str(new_water_meter.uuid),
        "value": 11,
        "month": 3,
        "year": 2023
    }
    response = make_put_request_with_json_response(
        client, f"/api/water_meters/history/{water_meter_history.uuid}/", data=water_meter_history_new_data
    )
    assert response.status_code == 200, response.data
    expected_response_data = {
        "uuid": str(water_meter_history.uuid),
        **water_meter_history_new_data
    }
    assert response.data == expected_response_data, response.data


@pytest.mark.django_db
def test_delete(client: Client):
    authenticate_user(client, ADMIN_AUTHENTICATION_CREDENTIALS)

    building = Building.objects.create(address="address")
    apartment = Apartment.objects.create(
        building=building,
        number=1,
        area=100.1,
        water_tariff=None,
        area_tariff=None
    )
    water_meter = WaterMeter.objects.create(
        mark="Some mark",
        apartment=apartment
    )
    water_meter_history = WaterMeterHistory.objects.create(
        meter=water_meter,
        value=10,
        month=1,
        year=2024
    )
    response = make_delete_request_with_json_response(client, f"/api/water_meters/history/{water_meter_history.uuid}/")
    assert response.status_code == 204, response.data
    assert not WaterMeterHistory.objects.filter(uuid=water_meter.uuid).exists()
