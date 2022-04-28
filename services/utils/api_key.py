import os
import secrets


FILE = ".api-key"


def generate_api_key(number_of_characters: int) -> str:
    api_key = secrets.token_urlsafe(nbytes=number_of_characters)

    with open(FILE, "w") as file:
        file.write(api_key)

    return api_key


def get_or_create_api_key(number_of_characters: int = 128) -> str:
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return file.read()

    return generate_api_key(number_of_characters)
