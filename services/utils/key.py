import os
import secrets
import string


API_KEY_FILE = ".api-key"
SECRET_KEY_FILE = ".secret-key"


def generate_key(number_of_characters: int) -> str:
    alphabet = string.digits + string.ascii_letters + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(number_of_characters))


def get_or_create_api_key(
    number_of_characters: int = 128, force_create: bool = False
) -> str:
    return _get_or_create_key(
        API_KEY_FILE,
        number_of_characters=number_of_characters,
        force_create=force_create,
    )


def get_or_create_secret_key(number_of_characters: int = 128) -> str:
    return _get_or_create_key(
        SECRET_KEY_FILE,
        number_of_characters=number_of_characters,
    )


def _get_or_create_key(
    file_name: str, number_of_characters: int = 128, force_create: bool = False
) -> str:
    if not force_create and os.path.exists(file_name):
        with open(file_name, "r") as file:
            return file.read()
    else:
        key = generate_key(number_of_characters)
        with open(file_name, "w") as file:
            file.write(key)
        return key
