from typing import Optional

from blacksheep import Request
from guardpost.asynchronous.authentication import AuthenticationHandler, Identity

import settings


class ApiKeyAuthHandler(AuthenticationHandler):
    api_key: str

    def __init__(self):
        self.api_key = settings.API_KEY

    async def authenticate(self, context: Request) -> Optional[Identity]:
        header_key = context.get_first_header(b"api-key")

        if self.api_key and isinstance(header_key, bytes):
            key = header_key.decode("utf-8")
            context.identity = Identity({}, "API_KEY") if key == self.api_key else None
        elif not self.api_key:
            context.identity = Identity({}, "PUBLIC")
        else:
            context.identity = None

        return context.identity
