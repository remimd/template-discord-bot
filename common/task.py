import asyncio
from abc import ABC, abstractmethod
from threading import Thread

from services import logs


class ParallelTask(Thread, ABC):
    seconds: float

    def __init__(
        self, days: float = 0, hours: float = 0, minutes: float = 0, seconds: float = 0
    ):
        name = self.__class__.__name__
        super(ParallelTask, self).__init__(name=name, daemon=True)
        self.seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds

    def clone(self):
        return self.__class__()

    def start(self):
        super(ParallelTask, self).start()
        logs.ok(f'Parallel Task: "{self.name}" ready')

    def run(self):
        coroutine = self._loop()
        asyncio.run(coroutine)

    async def _loop(self):
        while True:
            await self.execute()
            await asyncio.sleep(self.seconds)

    @abstractmethod
    async def execute(self):
        pass
