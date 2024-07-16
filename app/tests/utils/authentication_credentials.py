from dataclasses import dataclass


@dataclass
class AuthenticationCredentials:
    username: str
    password: str

    @property
    def as_dict(self):
        return {
            "username": self.username,
            "password": self.password
        }


ADMIN_AUTHENTICATION_CREDENTIALS = AuthenticationCredentials("admin", "password")
