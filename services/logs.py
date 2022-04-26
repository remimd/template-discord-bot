import os
import traceback

from colorama import Fore, Style

from services.utils import dates


_logs: list[str] = []


def log(message: str, state: str, color: str = ""):
    text = f"{state.upper()}:     [{dates.now()}]: {message}"
    styled_text = (
        f"{Style.BRIGHT}{color}{state.upper()}{Style.RESET_ALL}:     "
        f"[{Fore.LIGHTBLACK_EX}{dates.now()}{Style.RESET_ALL}]: {message}"
    )
    _add(text)
    print(styled_text)


def ok(message: str):
    log(message, "ok", color=Fore.GREEN)


def info(message: str):
    log(message, "info", color=Fore.BLUE)


def warning(message: str):
    log(message, "warning", color=Fore.YELLOW)


def error(message: str):
    log(message, "error", color=Fore.RED)


def exception(exc: BaseException):
    message = "\n".join([line.rstrip("\n") for line in traceback.format_exception(exc)])
    log(message, "exception", color=Fore.RED)


def _add(message: str):
    _logs.append(message)


def save(directory: str = "logs"):
    if not os.path.exists(directory):
        os.mkdir(directory)
    with open(
        os.path.join(directory, f"{dates.now(dates.files_format)}.txt"), "w"
    ) as file:
        file.write("\n".join(_logs))
    log("Logs saved", "logs", color=Fore.CYAN)
