import os

from openapidocs.v3 import Info

from services.utils.api_key import get_or_create_api_key


# Discord Bot
TOKEN = os.getenv("TOKEN")

# API
APP_NAME = os.getenv("APP_NAME", "Discord Bot API")
APP_VERSION = os.getenv("APP_VERSION", "1.0")
APP_INFO = Info(title=APP_NAME, version=APP_VERSION)

API_KEY = os.getenv("API_KEY", get_or_create_api_key())

DEBUG = False

# Django ORM
INSTALLED_APPS = ("django_extensions", "core")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", "discord_bot_api"),
        "USER": os.getenv("DB_USER", "root"),
        "PASSWORD": os.getenv("DB_PASSWORD", "root"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", 5432),
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
