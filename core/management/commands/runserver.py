from typing import Any

import uvicorn
from django.core.management import CommandParser
from django.core.management.commands.runserver import Command as BaseRunServerCommand

from services import logs


class Command(BaseRunServerCommand):
    default_port = 8000

    def add_arguments(self, parser: CommandParser):
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
            "-r",
            "--reload",
            action="store_true",
            help="auto reload on change",
            dest="reload",
        )

    def parse_uvicorn_options(self, **options) -> dict[str, Any]:
        return {
            "port": options.get("port") or self.default_port,
            "reload": options.get("reload") or False,
        }

    def handle(self, *args, **options):
        uvicorn_options = self.parse_uvicorn_options(**options)
        uvicorn.run("core:application", **uvicorn_options)

        if options.get("save_logs"):
            logs.save()
