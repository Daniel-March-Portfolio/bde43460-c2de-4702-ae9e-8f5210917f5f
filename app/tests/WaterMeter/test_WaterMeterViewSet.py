import pytest
from django.test import Client

from Apartment.models import Apartment
from Building.models import Building
from WaterMeter.models import WaterMeter
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

    response = make_get_request_with_json_response(client, f"/api/water_meters/{water_meter.uuid}/")
    assert response.status_code == 200, response.data
    expected_response_data = {
        "uuid": str(water_meter.uuid),
        "mark": "Some mark",
        "apartment": str(water_meter.apartment.uuid)
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

    water_meter_1 = WaterMeter.objects.create(
        mark="Some mark 1",
        apartment=apartment
    )
    water_meter_2 = WaterMeter.objects.create(
        mark="Some mark 2",
        apartment=apartment
    )

    response = make_get_request_with_json_response(client, f"/api/water_meters/")
    assert response.status_code == 200, response.data
    water_meter_1_data = {
        "uuid": str(water_meter_1.uuid),
        "mark": "Some mark 1",
        "apartment": str(apartment.uuid)
    }
    water_meter_2_data = {
        "uuid": str(water_meter_2.uuid),
        "mark": "Some mark 2",
        "apartment": str(apartment.uuid)
    }
    expected_response_data = sorted([water_meter_1_data, water_meter_2_data], key=lambda x: x["uuid"])
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
    water_meter_data = {
        "mark": "Some mark",
        "apartment": str(apartment.uuid)
    }
    response = make_post_request_with_json_response(client, f"/api/water_meters/", data=water_meter_data)
    assert response.status_code == 201, response.data
    expected_response_data = {
        "uuid": str(WaterMeter.objects.first().uuid),
        **water_meter_data
    }
    assert response.data == expected_response_data, response.data


@pytest.mark.django_db
def test_update(client: Client):
    authenticate_user(client, ADMIN_AUTHENTICATION_CREDENTIALS)

    building = Building.objects.create(address="address")
    apartment = Apartment(
        building=building,
        number=1,
        area=100,
        water_tariff=None,
        area_tariff=None
    )
    new_apartment = Apartment.objects.create(
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
    apartment_new_data = {
        "mark": "New mark",
        "apartment": str(new_apartment.uuid)
    }
    response = make_put_request_with_json_response(
        client, f"/api/water_meters/{water_meter.uuid}/", data=apartment_new_data
    )
    assert response.status_code == 200, response.data
    expected_response_data = {
        "uuid": str(water_meter.uuid),
        **apartment_new_data
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
    response = make_delete_request_with_json_response(client, f"/api/water_meters/{water_meter.uuid}/")
    assert response.status_code == 204, response.data
    assert not WaterMeter.objects.filter(uuid=water_meter.uuid).exists()
