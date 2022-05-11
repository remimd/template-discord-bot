from datetime import datetime

from common.static_class import StaticClass


class Format(StaticClass):
    LOG = "%b-%d-%Y %H:%M:%S"
    FILE = "%Y-%m-%d_%H-%M-%S"
    MESSAGE = "%B %d, %Y ~ %H:%M:%S"
    DROP = "%B %d, %Y ~ %H:%M:%S.%f"


def now(format: str = Format.LOG) -> str:
    return datetime.now().strftime(format)
