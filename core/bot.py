from discord import Client

import settings


class Bot(Client):
    _token: str

    def __init__(self, **options):
        Client.__init__(self, **options)
        self._token = settings.TOKEN

    def run(self, *args, **kwargs):
        if self._token:
            args = (self._token,) + args
            Client.run(self, *args, **kwargs)
        else:
            raise ValueError("Token undefined.")
