from blacksheep import Response
from blacksheep.server.controllers import ApiController, get, post
from blacksheep.server.responses import ok, not_modified, pretty_json

from core.discord.bot import Bot


class BotController(ApiController):
    bot: Bot

    def __init__(self):
        self.bot = Bot.get_instance()

    @classmethod
    def class_name(cls) -> str:
        return "Bot Controller"

    @classmethod
    def route(cls) -> str:
        return "bot"

    @get("/disable")
    def is_disabled(self) -> Response:
        return pretty_json({"value": self.bot.disable})

    @post("/disable")
    def disable(self) -> Response:
        if self.bot.disable:
            return not_modified()

        self.bot.disable = True
        return ok()

    @get("/enable")
    def is_enabled(self) -> Response:
        return pretty_json({"value": not self.bot.disable})

    @post("/enable")
    def enable(self) -> Response:
        if not self.bot.disable:
            return not_modified()

        self.bot.disable = False
        return ok()
