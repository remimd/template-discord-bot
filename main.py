from blacksheep import Application
from blacksheep.server.openapi.v3 import OpenAPIHandler

import api  # noqa
import settings
from core.bot import Bot


app = Application(show_error_details=settings.DEBUG)
swagger = OpenAPIHandler(info=settings.APP_INFO)
swagger.bind_app(app)


@app.after_start
async def after_start(_):
    bot = Bot.get_instance()
    bot.run_in_event_loop()
