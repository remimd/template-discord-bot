import os


def set_environment():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")
