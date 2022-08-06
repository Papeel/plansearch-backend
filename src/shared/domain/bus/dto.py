"""DTO. """

from dataclasses import dataclass, fields

from src.shared.domain.exceptions import DtoUnacceptedPropertyError, DtoPropertyCanNotBeEmptyError, \
    DtoRequiredPropertyError
from src.shared.domain.null import Null
from src.shared.domain.utils import is_optional


@dataclass(frozen=True)
class DTO:

    def __init__(self, *args, **kwargs): pass

    @classmethod
    def from_dict(cls, dict_obj: dict):

        class_property_names: list = [field.name for field in fields(cls)]

        for k, v in dict_obj.items():
            if k not in class_property_names:
                raise DtoUnacceptedPropertyError(
                    f'{k} is an unaccepted field')

        for field in fields(cls):
            if not dict_obj.get(field.name) and \
                    dict_obj.get(field.name) is not None and \
                    not isinstance(dict_obj.get(field.name), int) and \
                    not isinstance(dict_obj.get(field.name), float):
                raise DtoPropertyCanNotBeEmptyError(
                    f'{field.name} can not be empty. Use null or assign a value')

            if dict_obj.get(field.name) is None and \
                    not is_optional(field.type) and not isinstance(field.default, Null) \
                    or (isinstance(field.default, list) and len(field.default) and not isinstance(field.default[0], Null)):
                raise DtoRequiredPropertyError(
                    f'{field.name} is required')

        return cls(**dict_obj)
