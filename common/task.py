from __future__ import annotations

import asyncio
from abc import ABC, abstractmethod
from threading import Thread

from services import logs


_tasks_list: list[AbstractTask] = []


def get_tasks_list() -> list[AbstractTask]:
    return _tasks_list


class AbstractTask(ABC):
    disable: bool
    name: str

    def __new__(cls, *args, **kwargs):
        instance = super(AbstractTask, cls).__new__(cls)
        _tasks_list.append(instance)
        return instance

    def __init__(self, name: str = None):
        self.disable = False
        self.name = name or self.__class__.__name__

    def __str__(self) -> str:
        return self.name

    @abstractmethod
    def start(self):
        raise NotImplementedError


class ParallelTask(Thread, AbstractTask, ABC):
    seconds: float

    def __init__(
        self,
        name: str = None,
        days: float = 0,
        hours: float = 0,
        minutes: float = 0,
        seconds: float = 0,
    ):
        Thread.__init__(self, daemon=True)
        AbstractTask.__init__(self, name=name)
        self.seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds

    def start(self):
        Thread.start(self)
        logs.ok(f'Parallel Task: "{self}" ready')

    def run(self):
        coroutine = self._loop()
        asyncio.run(coroutine)

    async def _loop(self):
        while True:
            if self.disable:
                continue

            await self.execute()
            await asyncio.sleep(self.seconds)

    @abstractmethod
    async def execute(self):
        raise NotImplementedError
