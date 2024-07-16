import json
from json import JSONDecodeError

from django.http import HttpResponse


def load_json_from_django_http_response(response: HttpResponse) -> dict:
    return json.loads(response.content.decode("utf-8"))


def try_to_load_json_from_django_http_response_or_empty_dict(response: HttpResponse) -> dict:
    try:
        return load_json_from_django_http_response(response)
    except JSONDecodeError:
        return {}
