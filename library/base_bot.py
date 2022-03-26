from __future__ import annotations

from discord import Intents
from discord.ext.commands import Bot
from discord_slash import SlashCommand

import settings
from services.utils import logs


class BaseBot(Bot):
    _instance: BaseBot | None = None
    _slash: SlashCommand
    _token: str

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            raise RuntimeError(f"{cls.__name__} can only be built once.")
        else:
            cls._instance = super(BaseBot, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, **options):
        if not options.get("intents", None):
            options["intents"] = BaseBot._generate_intents()
        super(BaseBot, self).__init__("", help_command=None, **options)
        self._slash = SlashCommand(self, sync_commands=True)
        self._token = settings.TOKEN

    def __str__(self) -> str:
        return self.user.display_name if self.user else self.__class__.__name__

    @classmethod
    def get_instance(cls) -> BaseBot:
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    @staticmethod
    def _generate_intents() -> Intents:
        intents = Intents.default()
        intents.members = True
        intents.messages = False
        return intents

    def run(self, *args, **kwargs):
        logs.info("Starting...")
        if self._token:
            args = (self._token,) + args
            super(BaseBot, self).run(*args, **kwargs)
        else:
            raise ValueError("Token undefined.")

    async def on_ready(self):
        logs.ok(f"{self} is ready")

    async def close(self):
        logs.info("Shutdown...")
        await super(BaseBot, self).close()
        logs.ok(f"{self} is stopped")

    def command(
        self,
        name: str,
        description: str = None,
        guild_ids: list[int] = None,
        options: list[dict] = None,
        default_permission: bool = True,
        permissions: dict = None,
        connector: dict = None,
    ):
        return self._slash.slash(
            name=name,
            description=description,
            guild_ids=guild_ids,
            options=options,
            default_permission=default_permission,
            permissions=permissions,
            connector=connector,
        )
