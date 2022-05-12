from datetime import datetime

from common.static_class import StaticClass


class Format(StaticClass):
    DROP = "%B %d, %Y ~ %H:%M:%S.%f"
    FILE = "%Y-%m-%d_%H-%M-%S"
    LOG = "%b-%d-%Y %H:%M:%S"
    MESSAGE = "%B %d, %Y ~ %H:%M:%S"


def now(format: str = Format.LOG) -> str:
    return datetime.now().strftime(format)
