from blacksheep import Application
from blacksheep.server.openapi.v3 import OpenAPIHandler
from blacksheep.server.authorization import Policy
from guardpost.common import AuthenticatedRequirement

import settings
from . import controllers
from .authentication import ApiKeyAuthHandler


application = Application(show_error_details=settings.DEBUG)
swagger = OpenAPIHandler(info=settings.APP_INFO)
swagger.bind_app(application)

authentication = application.use_authentication()
authentication.add(ApiKeyAuthHandler())

authorization = application.use_authorization()
authorization.default_policy = Policy("authenticated", AuthenticatedRequirement())
