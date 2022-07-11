from typing import Any, Type

from blacksheep import Response, bad_request, created, not_found, ok
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model

from common.api.serializer import Serializer


class Crud:
    model: Type[Model]
    serializer: Serializer

    def __init__(self, model: Type[Model], serializer: Serializer):
        self.model = model
        self.serializer = serializer

    @property
    def model_name(self) -> str:
        return self.model.__name__

    def get_list(self) -> list[object]:
        object_list = self.model.objects.all()
        return [self.serializer.serialize(o) for o in object_list]

    def get_by_pk(self, pk: int | str) -> object | Response:
        try:
            o = self.model.objects.get(pk=pk)
            return self.serializer.serialize(o)
        except ObjectDoesNotExist:
            return not_found()

    def create(self, values: dict[str, Any]) -> Response:
        try:
            o = self.model.objects.create(**values)
            o.save()
        except TypeError as exc:
            return bad_request(str(exc))

        return created()

    def edit(self, pk: int | str, values: dict[str, Any]) -> Response:
        try:
            o = self.model.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return not_found()

        for key, value in values.items():
            if not hasattr(o, key):
                return bad_request(f"{self.model_name} doesn't have attribute '{key}'.")

            setattr(o, key, value)

        o.save()
        return ok()

    def delete(self, pk: int | str) -> Response:
        try:
            o = self.model.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return not_found()

        o.delete()
        return ok()
