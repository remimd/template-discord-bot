import os
import secrets


FILE = ".api-key"


def generate_api_key() -> str:
    api_key = secrets.token_urlsafe(32)

    with open(FILE, "w") as file:
        file.write(api_key)

    return api_key


def get_or_create_api_key() -> str:
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return file.read()

    return generate_api_key()
