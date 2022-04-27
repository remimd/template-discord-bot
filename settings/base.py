import os

from openapidocs.v3 import Info

from services.api import get_or_create_api_key


# Discord Bot
TOKEN = os.getenv("TOKEN")

# API
APP_NAME = os.getenv("APP_NAME", "Discord Bot API")
APP_VERSION = os.getenv("APP_VERSION", "1.0")
APP_INFO = Info(title=APP_NAME, version=APP_VERSION)

API_KEY = os.getenv("API_KEY", get_or_create_api_key())

DEBUG = False
