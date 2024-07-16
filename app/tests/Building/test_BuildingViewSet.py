import pytest
from django.test import Client

from Building.models import Building
from tests.utils.authenticate_user import authenticate_user
from tests.utils.authentication_credentials import ADMIN_AUTHENTICATION_CREDENTIALS
from tests.utils.request import make_get_request_with_json_response, make_post_request_with_json_response, \
    make_delete_request_with_json_response, make_put_request_with_json_response


@pytest.mark.django_db
def test_retrieve(client: Client):
    authenticate_user(client, ADMIN_AUTHENTICATION_CREDENTIALS)

    building = Building.objects.create(address="address")

    response = make_get_request_with_json_response(client, f"/api/buildings/{building.uuid}/")
    assert response.status_code == 200, response.data
    expected_response_data = {
        "uuid": str(building.uuid),
        "address": building.address
    }
    assert response.data == expected_response_data, response.data


@pytest.mark.django_db
def test_list(client: Client):
    authenticate_user(client, ADMIN_AUTHENTICATION_CREDENTIALS)

    building_1 = Building.objects.create(
        address="address1"
    )
    building_2 = Building.objects.create(
        address="address2"
    )

    response = make_get_request_with_json_response(client, f"/api/buildings/")
    assert response.status_code == 200, response.data
    building_1_data = {
        "uuid": str(building_1.uuid),
        "address": building_1.address
    }
    building_2_data = {
        "uuid": str(building_2.uuid),
        "address": building_2.address
    }
    expected_response_data = sorted([building_1_data, building_2_data], key=lambda x: x["uuid"])
    got_response_data = sorted(response.data, key=lambda x: x["uuid"])
    assert got_response_data == expected_response_data, response.data


@pytest.mark.django_db
def test_create(client: Client):
    authenticate_user(client, ADMIN_AUTHENTICATION_CREDENTIALS)

    building_data = {
        "address": "address",
    }
    response = make_post_request_with_json_response(client, f"/api/buildings/", data=building_data)
    assert response.status_code == 201, response.data
    expected_response_data = {
        "uuid": str(Building.objects.first().uuid),
        **building_data
    }
    assert response.data == expected_response_data, response.data


@pytest.mark.django_db
def test_update(client: Client):
    authenticate_user(client, ADMIN_AUTHENTICATION_CREDENTIALS)

    building = Building.objects.create(address="address")
    building_new_data = {
        "address": "new address",
    }
    response = make_put_request_with_json_response(
        client, f"/api/buildings/{building.uuid}/", data=building_new_data
    )
    assert response.status_code == 200, response.data
    expected_response_data = {
        "uuid": str(building.uuid),
        **building_new_data
    }
    assert response.data == expected_response_data, response.data


@pytest.mark.django_db
def test_delete(client: Client):
    authenticate_user(client, ADMIN_AUTHENTICATION_CREDENTIALS)

    building = Building.objects.create(address="address")
    response = make_delete_request_with_json_response(client, f"/api/buildings/{building.uuid}/")
    assert response.status_code == 204, response.data
    assert not Building.objects.filter(uuid=building.uuid).exists()
