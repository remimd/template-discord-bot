import os
from argparse import ArgumentParser, Namespace

from libraries import server


_commands = {
    "makemigrations": server.makemigrations,
    "migrate": server.migrate,
    "runserver": server.runserver,
}


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    args = parse_arguments().__dict__
    command = args.pop("command")
    _commands[command](**args)


def parse_arguments() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("command", choices=_commands.keys())
    parser.add_argument(
        "-p", "--port", default=8000, type=int, help="change port", dest="port"
    )
    parser.add_argument(
        "-l", "--logs", action="store_true", help="save custom logs", dest="save_logs"
    )
    return parser.parse_args()


if __name__ == "__main__":
    main()
