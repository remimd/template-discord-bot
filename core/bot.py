from discord import Client
from discord_slash import SlashCommand

import settings
from services import logs


class Bot(Client):
    _slash: SlashCommand
    _token: str

    def __init__(self, **options):
        Client.__init__(self, **options)
        self._slash = SlashCommand(self)
        self._token = settings.TOKEN

    def run(self, *args, **kwargs):
        logs.info("Starting...")
        if self._token:
            args = (self._token,) + args
            Client.run(self, *args, **kwargs)
        else:
            raise ValueError("Token undefined.")

    async def on_ready(self):
        logs.ok(f"{self.user.display_name} is ready")

    async def close(self):
        logs.info("Shutdown...")
        await Client.close(self)
        logs.ok(f"{self.user.display_name} is stopped")
