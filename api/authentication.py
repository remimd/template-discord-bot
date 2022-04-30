from typing import Optional

from blacksheep import Request
from django.conf import settings
from guardpost.asynchronous.authentication import AuthenticationHandler, Identity


class ApiKeyAuthHandler(AuthenticationHandler):
    async def authenticate(self, context: Request) -> Optional[Identity]:
        header_key = context.get_first_header(b"x-api-key")
        api_key = settings.API_KEY

        if api_key and isinstance(header_key, bytes):
            key = header_key.decode("utf-8")
            context.identity = Identity({}, "API_KEY") if key == api_key else None
        elif not api_key:
            context.identity = Identity({}, "PUBLIC")
        else:
            context.identity = None

        return context.identity
