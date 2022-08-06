"""FilterField. """

from dataclasses import dataclass

from src.shared.domain.value_object import ValueObject


@dataclass(frozen=True)
class FilterField(ValueObject):
    value: str