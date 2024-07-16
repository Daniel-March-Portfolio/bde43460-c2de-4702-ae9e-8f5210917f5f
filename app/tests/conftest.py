import pytest
from django.contrib.auth.models import User

from tests.utils.authentication_credentials import ADMIN_AUTHENTICATION_CREDENTIALS


@pytest.fixture(scope="function", autouse=True)
def create_superuser():
    User.objects.create_superuser(**ADMIN_AUTHENTICATION_CREDENTIALS.as_dict)
