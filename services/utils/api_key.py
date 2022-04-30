import os
import secrets


FILE = ".api-key"


def generate_api_key(number_of_characters: int) -> str:
    return secrets.token_urlsafe(nbytes=number_of_characters)


def get_or_create_api_key(
    number_of_characters: int = 128, force_create: bool = False
) -> str:
    if not force_create and os.path.exists(FILE):
        with open(FILE, "r") as file:
            return file.read()
    else:
        api_key = generate_api_key(number_of_characters)
        with open(FILE, "w") as file:
            file.write(api_key)
        return api_key
