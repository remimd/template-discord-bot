import asyncio
from abc import ABC
from typing import Optional

from discord import Intents
from discord.ext.commands import Bot
from discord_slash import SlashCommand

import settings
from libraries.singleton import Singleton
from services import logs


class BaseBot(Bot, Singleton, ABC):
    disable: bool
    slash: SlashCommand
    _token: Optional[str]

    def __init__(self, **options):
        if not options.get("intents", None):
            options["intents"] = BaseBot._generate_intents()

        Bot.__init__(self, "", help_command=None, **options)

        self.disable = False
        self.slash = SlashCommand(self, sync_commands=True)
        self._token = settings.TOKEN

    def __str__(self) -> str:
        return self.user.display_name if self.user else self.__class__.__name__

    @staticmethod
    def _generate_intents() -> Intents:
        intents = Intents.default()
        intents.members = True
        intents.messages = False
        return intents

    def run_in_event_loop(self, *args, **kwargs):
        async def run():
            try:
                await self.start(*args, **kwargs)
            finally:
                if not self.is_closed():
                    await self.close()

        asyncio.ensure_future(run(), loop=self.loop)

    async def start(self, *args, **kwargs):
        logs.info("Starting...")
        if self._token:
            args = (self._token,) + args
            await super(BaseBot, self).start(*args, **kwargs)
        else:
            raise ValueError("Token undefined.")

    async def on_ready(self):
        logs.ok(f"{self} is ready")

    async def close(self):
        logs.info("Shutdown...")
        await super(BaseBot, self).close()
        logs.warning(f"{self} is stopped")

    def check_disable(self):
        if self.disable:
            raise RuntimeError("Bot is disabled.")
