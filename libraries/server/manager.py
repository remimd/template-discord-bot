from typing import Callable, Iterable

from libraries.singleton import Singleton


class ServerManager(Singleton):
    _commands: dict[str, Callable]

    def __init__(self):
        self._commands = {}
        from . import commands  # noqa

    @property
    def commands_list(self) -> Iterable[str]:
        return self._commands.keys()

    def get_command(self, name: str) -> Callable:
        return self._commands[name]

    def add_command(self, name: str, function: Callable):
        self._commands[name] = function

    def command(self, function: Callable):
        self.add_command(function.__name__, function)
