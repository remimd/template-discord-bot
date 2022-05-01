import uvicorn
from django.core.management import CommandParser
from django.core.management.commands.runserver import Command as BaseRunServerCommand

from api import application
from core.discord.bot import Bot
from services import logs


class Command(BaseRunServerCommand):
    default_port = 8000

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            "-p",
            "--port",
            default=self.default_port,
            type=int,
            help="change port",
            dest="port",
        )
        parser.add_argument(
            "-l",
            "--logs",
            action="store_true",
            help="save custom logs",
            dest="save_logs",
        )

    def handle(self, *args, **options):
        @application.after_start
        async def start_bot(_):
            bot = Bot.get_instance()
            bot.run_in_event_loop()

        uvicorn_options = {
            "port": options.get("port") or self.default_port,
        }

        uvicorn.run(application, **uvicorn_options)

        if options.get("save_logs"):
            logs.save()
