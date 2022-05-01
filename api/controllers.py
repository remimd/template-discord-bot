from blacksheep import Response
from blacksheep.server.controllers import ApiController, get, post
from blacksheep.server.responses import ok, pretty_json

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
    def is_disable(self) -> Response:
        return pretty_json({"value": self.bot.disable})

    @post("/disable")
    def disable(self) -> Response:
        if self.bot.disable:
            return Response(status=304)

        self.bot.disable = True
        return ok()

    @get("/unable")
    def is_unable(self) -> Response:
        return pretty_json({"value": not self.bot.disable})

    @post("/unable")
    def unable(self) -> Response:
        if not self.bot.disable:
            return Response(status=304)

        self.bot.disable = False
        return ok()
