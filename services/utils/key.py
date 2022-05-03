import os
import secrets
import string


API_KEY_FILE = ".api-key"
SECRET_KEY_FILE = ".secret-key"

DEFAULT_LENGTH = 128


def generate_key(length: int) -> str:
    alphabet = string.digits + string.ascii_letters + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(length))


def get_or_create_key(
    file_name: str, length: int = DEFAULT_LENGTH, force_create: bool = False
) -> str:
    if not force_create and os.path.exists(file_name):
        with open(file_name, "r") as file:
            return file.read()
    else:
        key = generate_key(length)
        with open(file_name, "w") as file:
            file.write(key)
        return key


def get_or_create_api_key(
    length: int = DEFAULT_LENGTH, force_create: bool = False
) -> str:
    return get_or_create_key(
        API_KEY_FILE,
        length=length,
        force_create=force_create,
    )


def get_or_create_secret_key(length: int = DEFAULT_LENGTH) -> str:
    return get_or_create_key(SECRET_KEY_FILE, length=length)
