from abc import ABC


class StaticClass(ABC):
    def __new__(cls, *args, **kwargs):
        raise RuntimeError(f"{cls.__name__} can't be instantiated.")
