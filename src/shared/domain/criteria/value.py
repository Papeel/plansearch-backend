"""FilterValue. """

from dataclasses import dataclass

from src.shared.domain.value_object import ValueObject


@dataclass(frozen=True)
class FilterValue(ValueObject):
    value: str