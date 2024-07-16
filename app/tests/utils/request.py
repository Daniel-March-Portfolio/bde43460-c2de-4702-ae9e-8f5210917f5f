from dataclasses import dataclass

from django.http import HttpResponse
from django.test import Client

from tests.utils.load_json_from_django_http_response import try_to_load_json_from_django_http_response_or_empty_dict


@dataclass
class JsonResponse:
    status_code: int
    data: dict


def make_get_request_with_json_response(client: Client, url: str) -> JsonResponse:
    response: HttpResponse = client.get(url)
    json_response = _create_json_response(response)
    return json_response


def make_post_request_with_json_response(client: Client, url: str, data: dict) -> JsonResponse:
    response: HttpResponse = client.post(url, data, content_type="application/json")
    json_response = _create_json_response(response)
    return json_response


def make_put_request_with_json_response(client: Client, url: str, data: dict) -> JsonResponse:
    response: HttpResponse = client.put(url, data, content_type="application/json")
    json_response = _create_json_response(response)
    return json_response


def make_delete_request_with_json_response(client: Client, url: str) -> JsonResponse:
    response: HttpResponse = client.delete(url)
    json_response = _create_json_response(response)
    return json_response


def _create_json_response(response: HttpResponse) -> JsonResponse:
    json_response = JsonResponse(
        status_code=response.status_code, data=try_to_load_json_from_django_http_response_or_empty_dict(response)
    )
    return json_response
