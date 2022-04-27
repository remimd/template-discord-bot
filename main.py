from blacksheep import Application
from blacksheep.server.openapi.v3 import OpenAPIHandler
from blacksheep.server.authorization import Policy
from guardpost.common import AuthenticatedRequirement

import api  # noqa
import settings
from api.authentication import ApiKeyAuthHandler
from core.bot import Bot


app = Application(show_error_details=settings.DEBUG)
swagger = OpenAPIHandler(info=settings.APP_INFO)
swagger.bind_app(app)

authentication = app.use_authentication()
authentication.add(ApiKeyAuthHandler())

authorization = app.use_authorization()
authorization.default_policy = Policy("authenticated", AuthenticatedRequirement())


@app.after_start
async def after_start(_):
    bot = Bot.get_instance()
    bot.run_in_event_loop()
