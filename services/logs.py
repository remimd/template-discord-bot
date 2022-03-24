import os
import traceback

from colorama import Fore, Style

from . import dates


_logs: list[str] = []


def display(text: str, color: str = ""):
    _add(str(text))
    print(f"{Style.BRIGHT}{color}{text}{Fore.RESET}")


def log(message: str, state: str, color: str = "", title: str = None):
    headline = f"{title.center(75, '-')}\n" if title else ""
    text = f"{headline}[{dates.now()}] [{state.upper()}] {message}"
    display(text, color=color)


def ok(message: str):
    log(message, "ok", color=Fore.GREEN)


def info(message: str):
    log(message, "info", color=Fore.BLUE)


def warning(message: str):
    log(message, "warning", color=Fore.YELLOW)


def error(message: str):
    log(message, "error", color=Fore.RED)


def exception(exc: BaseException, title: str = None):
    message = "\n".join([line.rstrip("\n") for line in traceback.format_exception(exc)])
    log(message, "exception", color=Fore.RED, title=title)


def _add(message: str):
    _logs.append(message)


def save(directory: str = "logs"):
    if not os.path.exists(directory):
        os.mkdir(directory)
    with open(
        os.path.join(directory, f"{dates.now(dates.files_format)}.txt"), "w"
    ) as file:
        file.write("\n".join(_logs))
    display("Logs saved", color=Fore.CYAN)
