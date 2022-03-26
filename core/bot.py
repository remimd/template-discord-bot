from library.base_bot import BaseBot


class Bot(BaseBot):
    def __init__(self):
        super(Bot, self).__init__()
        from core import commands  # noqa
