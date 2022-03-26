from __future__ import annotations
from typing import Callable

from discord.ext import commands
from discord_slash import SlashCommand

import settings
from services import logs


class Bot(commands.Bot):
    _instance: Bot = None
    _slash: SlashCommand
    _token: str

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            raise RuntimeError(f"{cls.__name__} can only be built once.")
        else:
            cls._instance = super(Bot, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, **options):
        super(Bot, self).__init__(None, help_command=None, **options)
        self._slash = SlashCommand(self)
        self._token = settings.TOKEN

    @classmethod
    def get_instance(cls) -> Bot:
        if not cls._instance:
            cls()
        return cls._instance

    def run(self, *args, **kwargs):
        logs.info("Starting...")
        if self._token:
            args = (self._token,) + args
            super(Bot, self).run(*args, **kwargs)
        else:
            raise ValueError("Token undefined.")

    async def on_ready(self):
        logs.ok(f"{self.user.display_name} is ready")

    async def close(self):
        logs.info("Shutdown...")
        await super(Bot, self).close()
        logs.ok(f"{self.user.display_name} is stopped")

    @property
    def command(self) -> Callable:
        return self._slash.slash
