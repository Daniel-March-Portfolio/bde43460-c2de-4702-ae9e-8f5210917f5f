import pytest
from django.test import Client

from Tariff.models import AreaTariff
from tests.utils.authenticate_user import authenticate_user
from tests.utils.authentication_credentials import ADMIN_AUTHENTICATION_CREDENTIALS
from tests.utils.request import make_get_request_with_json_response, make_post_request_with_json_response, \
    make_delete_request_with_json_response, make_put_request_with_json_response


@pytest.mark.django_db
def test_retrieve(client: Client):
    authenticate_user(client, ADMIN_AUTHENTICATION_CREDENTIALS)

    tariff = AreaTariff.objects.create(
        title="Area tariff",
        price=100
    )

    response = make_get_request_with_json_response(client, f"/api/tariffs/area/{tariff.uuid}/")
    assert response.status_code == 200, response.data
    expected_response_data = {
        "uuid": str(tariff.uuid),
        "title": tariff.title,
        "price": tariff.price
    }
    assert response.data == expected_response_data, response.data


@pytest.mark.django_db
def test_list(client: Client):
    authenticate_user(client, ADMIN_AUTHENTICATION_CREDENTIALS)

    tariff_1 = AreaTariff.objects.create(
        title="Area tariff 1",
        price=100
    )
    tariff_2 = AreaTariff.objects.create(
        title="Area tariff 2",
        price=200
    )

    response = make_get_request_with_json_response(client, f"/api/tariffs/area/")
    assert response.status_code == 200, response.data
    tariff_1_data = {
        "uuid": str(tariff_1.uuid),
        "title": "Area tariff 1",
        "price": 100
    }
    tariff_2_data = {
        "uuid": str(tariff_2.uuid),
        "title": "Area tariff 2",
        "price": 200
    }
    expected_response_data = sorted([tariff_1_data, tariff_2_data], key=lambda x: x["uuid"])
    got_response_data = sorted(response.data, key=lambda x: x["uuid"])
    assert got_response_data == expected_response_data, response.data


@pytest.mark.django_db
def test_create(client: Client):
    authenticate_user(client, ADMIN_AUTHENTICATION_CREDENTIALS)

    tariff_data = {
        "title": "Area tariff",
        "price": 200
    }
    response = make_post_request_with_json_response(client, f"/api/tariffs/area/", data=tariff_data)
    assert response.status_code == 201, response.data
    expected_response_data = {
        "uuid": str(AreaTariff.objects.first().uuid),
        **tariff_data
    }
    assert response.data == expected_response_data, response.data


@pytest.mark.django_db
def test_update(client: Client):
    authenticate_user(client, ADMIN_AUTHENTICATION_CREDENTIALS)

    tariff = AreaTariff.objects.create(
        title="title",
        price=100
    )
    tariff_new_data = {
        "title": "New area tariff title",
        "price": 200
    }
    response = make_put_request_with_json_response(
        client, f"/api/tariffs/area/{tariff.uuid}/", data=tariff_new_data
    )
    assert response.status_code == 200, response.data
    expected_response_data = {
        "uuid": str(tariff.uuid),
        **tariff_new_data
    }
    assert response.data == expected_response_data, response.data


@pytest.mark.django_db
def test_delete(client: Client):
    authenticate_user(client, ADMIN_AUTHENTICATION_CREDENTIALS)

    tariff = AreaTariff.objects.create(
        title="Area tariff",
        price=100
    )
    response = make_delete_request_with_json_response(client, f"/api/tariffs/area/{tariff.uuid}/")
    assert response.status_code == 204, response.data
    assert not AreaTariff.objects.filter(uuid=tariff.uuid).exists()
