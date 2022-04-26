import os

from openapidocs.v3 import Info


# Discord Bot
TOKEN = os.getenv("TOKEN", None)

# API
APP_NAME = os.getenv("APP_NAME", "Discord Bot API")
APP_VERSION = os.getenv("APP_VERSION", "1.0")
APP_INFO = Info(title=APP_NAME, version=APP_VERSION)

DEBUG = False
