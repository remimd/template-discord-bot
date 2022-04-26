import os

from colorama import Fore
from dotenv import load_dotenv

from services import logs

load_dotenv()

EXEC_PROFILE = os.getenv("EXEC_PROFILE", "dev")

match EXEC_PROFILE.lower():
    case "dev":
        from .dev import *  # noqa
    case "prod":
        from .prod import *  # noqa
    case "local":
        from .local import *  # noqa
    case _:
        raise RuntimeError("No suitable configuration found.")

logs.display(f'Profile set from "{EXEC_PROFILE.title()} Settings"', color=Fore.CYAN)
