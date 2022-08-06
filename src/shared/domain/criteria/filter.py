"""Filter. """

from typing import TypeVar
from dataclasses import dataclass

from src.shared.domain.criteria.value import FilterValue
from src.shared.domain.criteria.field import FilterField

Filter = TypeVar('Filter')

@dataclass(frozen=True)
class Filter:
    field: FilterField
    value: FilterValue

    @classmethod
    def from_values(cls, values: dict[str, str]) -> Filter:
        return cls(
            FilterField(list(values.keys())[0]),
            FilterValue(list(values.values())[0])
        )

    def serialize(self) -> str:
        return f'{self.field.value, self.value.value}'