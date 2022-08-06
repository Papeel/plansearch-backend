"""Filters. """

from dataclasses import dataclass, field
from functools import reduce

from src.shared.domain.criteria.filter import Filter


@dataclass
class Filters:
    filters: list[Filter] = field(default_factory=list)

    @classmethod
    def from_values(cls, filters: dict[str, str]):
        return cls([Filter.from_values({k: v}) for k, v in filters.items()])

    def serialize(self):
        return reduce(lambda x, y: f'{x}{y.serialize()}', self.filters, '')

    def filters_to_primitives(self) -> dict:
        return {filter.field.value: filter.value.value for filter in self.filters}