from datetime import datetime


logs_format = "%b-%d-%Y %H:%M:%S"
files_format = "%Y-%m-%d_%H-%M-%S"
messages_format = "%B %d, %Y ~ %H:%M:%S"
drops_format = "%B %d, %Y ~ %H:%M:%S.%f"


def now(format: str = logs_format) -> str:
    return datetime.now().strftime(format)
