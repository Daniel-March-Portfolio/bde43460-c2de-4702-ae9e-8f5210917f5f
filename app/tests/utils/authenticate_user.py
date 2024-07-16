from django.test import Client

from tests.utils.authentication_credentials import AuthenticationCredentials


def authenticate_user(client: Client, authentication_credentials: AuthenticationCredentials):
    client.login(username=authentication_credentials.username, password=authentication_credentials.password)
