import uvicorn
from django.core.management import execute_from_command_line

from api import application
from core.discord.bot import Bot
from services import logs


def makemigrations(**kwargs):
    execute_from_command_line(argv=[__file__, "makemigrations"])


def migrate(**kwargs):
    execute_from_command_line(argv=[__file__, "migrate"])


def runserver(save_logs: bool = False, **kwargs):
    @application.after_start
    async def start_bot(_):
        bot = Bot.get_instance()
        bot.run_in_event_loop()

    uvicorn.run(application, **kwargs)

    if save_logs:
        logs.save()
