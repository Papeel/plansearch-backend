"""Utils. """

import re
from typing import get_origin, Union, get_args
from uuid import UUID


class Utils:

    @staticmethod
    def is_valid_uuid(value: str):
        try:
            UUID(str(value))
            return True
        except ValueError:
            return False


def camel_to_snake(value: str):
    value = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', value)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', value).lower()


def is_optional(obj: object) -> bool:
    return get_origin(obj) is Union and type(None) in get_args(obj)