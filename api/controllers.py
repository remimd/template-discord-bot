from blacksheep import Response
from blacksheep.server.controllers import ApiController, post
from blacksheep.server.responses import ok

from core.bot import Bot


class BotController(ApiController):
    bot: Bot

    def __init__(self):
        self.bot = Bot.get_instance()

    @classmethod
    def class_name(cls) -> str:
        return "Bot Controller"

    @classmethod
    def route(cls) -> str:
        return "api"

    @post("/unable")
    def unable(self) -> Response:
        if not self.bot.disable:
            return Response(status=304)

        self.bot.disable = False
        return ok()

    @post("/disable")
    def disable(self) -> Response:
        if self.bot.disable:
            return Response(status=304)

        self.bot.disable = True
        return ok()
