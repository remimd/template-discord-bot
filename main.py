from argparse import ArgumentParser, Namespace

from core.bot import Bot
from services.utils import logs


def main(save_logs: bool = False):
    bot = Bot.get_instance()
    bot.run()
    if save_logs:
        logs.save()


def parse_arguments() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("-l", "--logs", help="save logs", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    main(args.logs)
