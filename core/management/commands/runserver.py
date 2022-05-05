import inspect
from typing import Any

import uvicorn
from django.core.management import CommandParser
from django.core.management.commands.runserver import Command as BaseRunServerCommand

from services import logs


class Command(BaseRunServerCommand):
    default_host: str = "localhost"
    default_port: int = 8000

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            "--forwarded-allow-ips",
            dest="forwarded_allow_ips",
        )
        parser.add_argument(
            "-H",
            "--host",
            default=self.default_host,
            help="change host",
            dest="host",
        )
        parser.add_argument(
            "-l",
            "--logs",
            action="store_true",
            help="save custom logs",
            dest="save_logs",
        )
        parser.add_argument(
            "-p",
            "--port",
            default=self.default_port,
            type=int,
            help="change port",
            dest="port",
        )
        parser.add_argument(
            "--proxy-headers",
            action="store_true",
            dest="proxy_headers",
        )
        parser.add_argument(
            "-r",
            "--reload",
            action="store_true",
            help="auto reload on change",
            dest="reload",
        )
        parser.add_argument(
            "--ssl-certfile",
            dest="ssl_certfile",
        )
        parser.add_argument(
            "--ssl-keyfile",
            dest="ssl_keyfile",
        )

    def handle(self, *args, **options):
        uvicorn_options = self.parse_uvicorn_options(**options)
        uvicorn.run("core.asgi:application", **uvicorn_options)

        if options.get("save_logs"):
            logs.save()

    @staticmethod
    def parse_uvicorn_options(**options) -> dict[str, Any]:
        signature = inspect.signature(uvicorn.Config)
        keys = [
            parameter.name
            for parameter in signature.parameters.values()
            if parameter.kind == parameter.POSITIONAL_OR_KEYWORD
        ]
        return {key: value for key in keys if (value := options.get(key)) is not None}
