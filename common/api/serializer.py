from __future__ import annotations

import dataclasses
from types import NoneType
from typing import Iterable, Type

from django.db.models import Field, Model


_default_serializers: dict[Type[Model], Serializer] = {}


def get_default_serializer(model: Type[Model]) -> Serializer:
    return _default_serializers[model]


def get_or_create_default_serializer(
    model: Type[Model], dataclass: Type = None
) -> Serializer:
    return get_default_serializer(model) or set_default_serializer(
        model, Serializer(model, dataclass=dataclass)
    )


def set_default_serializer(model: Type[Model], serializer: Serializer) -> Serializer:
    _default_serializers[model] = serializer
    return serializer


class Serializer:
    VALID_TYPES = int, float, str, bool, NoneType

    model: Type[Model]
    dataclass: Type

    def __init__(self, model: Type[Model], dataclass: Type = None):
        self.model = model
        self.dataclass = dataclass or self.generate_dataclass()

    @property
    def model_fields(self) -> Iterable[Field]:
        return self.model._meta.get_fields()

    @classmethod
    def _serialize(cls, o: object) -> object:
        if isinstance(o, Model):
            serializer = get_or_create_default_serializer(o.__class__)
            o = serializer.serialize(o)
        elif isinstance(o, dict):
            o = {cls._serialize(key): cls._serialize(value) for key, value in o.items()}
        elif not isinstance(o, str) and isinstance(o, Iterable):
            o = [cls._serialize(value) for value in o]
        elif not isinstance(o, cls.VALID_TYPES):
            o = str(o)

        return o

    def serialize(self, instance: Model) -> object:
        if not isinstance(instance, self.model):
            raise TypeError(f"This instance isn't a {self.model.__name__}.")

        kwargs = {}
        fields = dataclasses.fields(self.dataclass)

        for field in fields:
            name = field.name
            value = getattr(instance, name)
            kwargs[name] = self._serialize(value)

        return self.dataclass(**kwargs)

    def generate_dataclass(self) -> Type:
        fields = [
            (field.name, object)
            for field in self.model_fields
            if isinstance(field, Field)
        ]

        return dataclasses.make_dataclass(
            f"Serialized{self.model.__name__}",
            fields,
            kw_only=True,
            slots=True,
        )
