import asyncio
from abc import ABC
from typing import Optional

from colorama import Fore
from discord import Intents, Message
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
        if not options.get("intents"):
            options["intents"] = BaseBot.generate_intents()

        super(BaseBot, self).__init__("💻", help_command=None, **options)
        self.disable = False
        self.slash = SlashCommand(self, sync_commands=True)
        self._token = settings.TOKEN

    def __str__(self) -> str:
        return self.user.display_name if self.user else self.__class__.__name__

    @staticmethod
    def generate_intents() -> Intents:
        intents = Intents.default()
        intents.members = True
        intents.presences = True
        return intents

    @staticmethod
    def log(message: str):
        logs.log(message, "discord", color=Fore.LIGHTBLUE_EX)

    def run_in_event_loop(self, *args, **kwargs):
        async def run():
            try:
                await self.start(*args, **kwargs)
            finally:
                if not self.is_closed():
                    await self.close()

        asyncio.ensure_future(run(), loop=self.loop)

    async def start(self, *args, **kwargs):
        self.log("Starting...")
        if self._token:
            args = (self._token,) + args
            await super(BaseBot, self).start(*args, **kwargs)
        else:
            raise ValueError("Token undefined.")

    async def on_ready(self):
        self.log(f"{self} is ready")

    async def close(self):
        self.log("Shutdown...")
        await super(BaseBot, self).close()
        self.log(f"{self} is stopped")

    async def on_message(self, message: Message):
        pass

    def command(self, *args, **kwargs):
        raise RuntimeError("This function is outdated, use 'bot.slash.slash'.")

    def check_disable(self):
        if self.disable:
            raise RuntimeError("Bot is disabled.")
