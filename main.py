import os
from argparse import ArgumentParser
from typing import Callable


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    command, kwargs = parse_arguments()
    command(**kwargs)


def parse_arguments() -> tuple[Callable, dict]:
    from libraries.server.manager import ServerManager

    manager = ServerManager.get_instance()
    parser = ArgumentParser()

    command_keyword = "command"
    parser.add_argument(command_keyword, choices=manager.commands_list)
    parser.add_argument(
        "-p", "--port", default=8000, type=int, help="change port", dest="port"
    )
    parser.add_argument(
        "-l", "--logs", action="store_true", help="save custom logs", dest="save_logs"
    )

    kwargs = parser.parse_args().__dict__
    key = kwargs.pop(command_keyword)
    command = manager.get_command(key)

    return command, kwargs


if __name__ == "__main__":
    main()
