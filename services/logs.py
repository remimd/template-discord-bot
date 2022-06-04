import logging
import os
import traceback

from colorama import Fore, Style

from services.utils.date_service import Format, now


_logger = logging.getLogger("custom_logs")
_logs: list[str] = []


def log(message: str, state: str, color: str = "", level: int = logging.INFO):
    text = _to_text(state.upper(), now(), message)
    styled_text = _to_text(
        f"{Style.BRIGHT}{color}{state.upper()}{Style.RESET_ALL}",
        f"{Fore.LIGHTBLACK_EX}{now()}{Style.RESET_ALL}",
        message,
    )
    _logger.log(level, text)
    _add(text)
    print(styled_text)


def ok(message: str):
    log(message, "ok", color=Fore.GREEN)


def info(message: str):
    log(message, "info", color=Fore.BLUE)


def warning(message: str):
    log(message, "warning", color=Fore.YELLOW, level=logging.WARNING)


def error(message: str):
    log(message, "error", color=Fore.RED, level=logging.ERROR)


def exception(exc: BaseException):
    message = "\n".join([line.rstrip("\n") for line in traceback.format_exception(exc)])
    log(message, "exception", color=Fore.RED, level=logging.ERROR)


def _to_text(state: str, date: str, message: str) -> str:
    return f"{state}:     [{date}]: {message}"


def _add(message: str):
    _logs.append(message)


def save(directory: str = "logs"):
    if not os.path.exists(directory):
        os.mkdir(directory)
    with open(os.path.join(directory, f"{now(format=Format.FILE)}.txt"), "w") as file:
        file.write("\n".join(_logs))
    log("Logs saved", "logs", color=Fore.CYAN)
