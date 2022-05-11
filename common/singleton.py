from __future__ import annotations

from abc import ABC
from typing import Optional


class Singleton(ABC):
    _instance: Optional[Singleton] = None

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            raise RuntimeError(f"{cls.__name__} can only be built once.")
        else:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls()
        return cls._instance
