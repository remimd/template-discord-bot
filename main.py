from argparse import ArgumentParser, Namespace

import uvicorn

from api import application
from core.bot import Bot
from services import logs


@application.after_start
async def start_bot(_):
    bot = Bot.get_instance()
    bot.run_in_event_loop()


def main(port: int = 8000, save_logs: bool = False):
    uvicorn.run(application, port=port)
    if save_logs:
        logs.save()


def parse_arguments() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "-p", "--port", default=8000, type=int, help="change port", dest="port"
    )
    parser.add_argument(
        "-l", "--logs", action="store_true", help="save custom logs", dest="save_logs"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    main(**args.__dict__)
