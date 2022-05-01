from libraries.discord.base_bot import BaseBot


class Bot(BaseBot):
    def __init__(self, **options):
        super(Bot, self).__init__(**options)
        from . import commands  # noqa
