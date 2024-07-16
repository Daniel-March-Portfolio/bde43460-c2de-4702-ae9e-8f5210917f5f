import pytest
from django.test import Client

from Apartment.models import Apartment
from Building.models import Building
from Tariff.models import WaterTariff, AreaTariff
from tests.utils.authenticate_user import authenticate_user
from tests.utils.authentication_credentials import ADMIN_AUTHENTICATION_CREDENTIALS
from tests.utils.request import make_get_request_with_json_response, make_post_request_with_json_response, \
    make_delete_request_with_json_response, make_put_request_with_json_response


@pytest.mark.django_db
def test_retrieve(client: Client):
    authenticate_user(client, ADMIN_AUTHENTICATION_CREDENTIALS)

    building = Building.objects.create(address="address")
    water_tariff = WaterTariff.objects.create(title="Water tariff", price=100)
    area_tariff = AreaTariff.objects.create(title="Area tariff", price=200)
    apartment = Apartment.objects.create(
        building=building,
        number=1,
        area=100.1,
        water_tariff=water_tariff,
        area_tariff=area_tariff
    )

    response = make_get_request_with_json_response(client, f"/api/apartments/{apartment.uuid}/")
    assert response.status_code == 200, response.data
    expected_response_data = {
        "uuid": str(apartment.uuid),
        "building": str(building.uuid),
        "number": 1,
        "area": 100.1,
        "water_tariff": str(water_tariff.uuid),
        "area_tariff": str(area_tariff.uuid)
    }
    assert response.data == expected_response_data, response.data


@pytest.mark.django_db
def test_list(client: Client):
    authenticate_user(client, ADMIN_AUTHENTICATION_CREDENTIALS)

    building = Building.objects.create(address="address")
    water_tariff = WaterTariff.objects.create(title="Water tariff", price=100)
    area_tariff = AreaTariff.objects.create(title="Area tariff", price=200)
    apartment_1 = Apartment.objects.create(
        building=building,
        number=1,
        area=100.1,
        water_tariff=None,
        area_tariff=area_tariff
    )
    apartment_2 = Apartment.objects.create(
        building=building,
        number=2,
        area=200.2,
        water_tariff=water_tariff,
        area_tariff=None
    )

    response = make_get_request_with_json_response(client, f"/api/apartments/")
    assert response.status_code == 200, response.data
    apartment_1_data = {
        "uuid": str(apartment_1.uuid),
        "building": str(building.uuid),
        "number": 1,
        "area": 100.1,
        "water_tariff": None,
        "area_tariff": str(area_tariff.uuid)
    }
    apartment_2_data = {
        "uuid": str(apartment_2.uuid),
        "building": str(building.uuid),
        "number": 2,
        "area": 200.2,
        "water_tariff": str(water_tariff.uuid),
        "area_tariff": None
    }
    expected_response_data = sorted([apartment_1_data, apartment_2_data], key=lambda x: x["uuid"])
    got_response_data = sorted(response.data, key=lambda x: x["uuid"])
    assert got_response_data == expected_response_data, response.data


@pytest.mark.django_db
def test_create(client: Client):
    authenticate_user(client, ADMIN_AUTHENTICATION_CREDENTIALS)

    building = Building.objects.create(address="address")
    water_tariff = WaterTariff.objects.create(title="Water tariff", price=100)
    area_tariff = AreaTariff.objects.create(title="Area tariff", price=200)
    apartment_data = {
        "building": str(building.uuid),
        "number": 1,
        "area": 100.1,
        "water_tariff": str(water_tariff.uuid),
        "area_tariff": str(area_tariff.uuid)
    }
    response = make_post_request_with_json_response(client, f"/api/apartments/", data=apartment_data)
    assert response.status_code == 201, response.data
    expected_response_data = {
        "uuid": str(Apartment.objects.first().uuid),
        **apartment_data
    }
    assert response.data == expected_response_data, response.data


@pytest.mark.django_db
def test_update(client: Client):
    authenticate_user(client, ADMIN_AUTHENTICATION_CREDENTIALS)

    building = Building.objects.create(address="address")
    water_tariff = WaterTariff.objects.create(title="Water tariff", price=100)
    area_tariff = AreaTariff.objects.create(title="Area tariff", price=200)
    apartment = Apartment.objects.create(
        building=building,
        number=1,
        area=100.1,
        water_tariff=None,
        area_tariff=area_tariff
    )
    apartment_new_data = {
        "building": str(building.uuid),
        "number": 1,
        "area": 100.1,
        "water_tariff": str(water_tariff.uuid),
        "area_tariff": None
    }
    response = make_put_request_with_json_response(
        client, f"/api/apartments/{apartment.uuid}/", data=apartment_new_data
    )
    assert response.status_code == 200, response.data
    expected_response_data = {
        "uuid": str(apartment.uuid),
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
        area=100,
        water_tariff=None,
        area_tariff=None
    )
    response = make_delete_request_with_json_response(client, f"/api/apartments/{apartment.uuid}/")
    assert response.status_code == 204, response.data
    assert not Apartment.objects.filter(uuid=apartment.uuid).exists()
