from datetime import datetime, tzinfo

from pytz import timezone

from common.static_class import StaticClass


class Format(StaticClass):
    DROP = "%B %d, %Y ~ %H:%M:%S.%f"
    FILE = "%Y-%m-%d_%H-%M-%S"
    LOG = "%b-%d-%Y %H:%M:%S"
    MESSAGE = "%B %d, %Y ~ %H:%M:%S"


def now(tz: tzinfo = timezone("Europe/Paris"), format: str = Format.LOG) -> str:
    date = datetime.now(tz).strftime(format)
    return date[:-4] if format.endswith("%f") else date
