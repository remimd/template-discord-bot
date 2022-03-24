import os

from colorama import Fore, Style
from dotenv import load_dotenv


load_dotenv()

BOLD = Style.BRIGHT
CYAN = Fore.CYAN
RESET = Fore.RESET

EXEC_PROFILE = os.environ.get("EXEC_PROFILE", "dev")

print(f'{BOLD}{CYAN}Profile set from "{EXEC_PROFILE.title()} Settings"{RESET}')

match EXEC_PROFILE:
    case "dev":
        from .dev import *  # noqa
    case "prod":
        from .prod import *  # noqa
    case "local":
        from .local import *  # noqa
    case _:
        RuntimeError("No suitable configuration found.")
