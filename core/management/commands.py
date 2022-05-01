import uvicorn
from django.core.management import execute_from_command_line

from api import application
from core.discord.bot import Bot
from core.management.manager import Manager
from services import logs


manager = Manager.get_instance()


@manager.command
def init_bdd():
    logs.info("Reset database")
    manager.call_command("reset_db")

    logs.info("Apply migrations")
    manager.call_command("migrate")


@manager.command
def makemigrations():
    execute_from_command_line(argv=[__file__, "makemigrations"])


@manager.command
def migrate():
    execute_from_command_line(argv=[__file__, "migrate"])


@manager.command
def reset_db():
    execute_from_command_line(argv=[__file__, "reset_db"])


@manager.command
def runserver(save_logs: bool = False, **kwargs):
    @application.after_start
    async def start_bot(_):
        bot = Bot.get_instance()
        bot.run_in_event_loop()

    uvicorn.run(application, **kwargs)

    if save_logs:
        logs.save()
