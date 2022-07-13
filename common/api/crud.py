from typing import Type

from blacksheep import Response, bad_request, created, not_found, ok, pretty_json
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model
from serpy import Serializer


class Crud:
    model: Type[Model]
    serializer: Type[Serializer]

    def __init__(self, model: Type[Model], serializer: Type[Serializer]):
        self.model = model
        self.serializer = serializer

    @property
    def model_name(self) -> str:
        return self.model.__name__

    def get_list(self) -> Response:
        object_list = self.model.objects.all()
        return pretty_json(self.serializer(object_list, many=True).data)

    def get_by_pk(self, primary_key) -> Response:
        try:
            o = self.model.objects.get(pk=primary_key)
            return pretty_json(self.serializer(o).data)
        except ObjectDoesNotExist:
            return not_found()

    def create(self, **kwargs) -> Response:
        try:
            o = self.model.objects.create(**kwargs)
            o.save()
        except TypeError as exc:
            return bad_request(str(exc))

        return created()

    def edit(self, primary_key, **kwargs) -> Response:
        try:
            o = self.model.objects.get(pk=primary_key)
        except ObjectDoesNotExist:
            return not_found()

        for key, value in kwargs.items():
            if not hasattr(o, key):
                return bad_request(f"{self.model_name} doesn't have attribute '{key}'.")

            setattr(o, key, value)

        o.save()
        return ok()

    def delete(self, primary_key) -> Response:
        try:
            o = self.model.objects.get(pk=primary_key)
        except ObjectDoesNotExist:
            return not_found()

        o.delete()
        return ok()
