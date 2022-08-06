"""Criteria. """

from dataclasses import dataclass

from src.shared.domain.criteria.order import Order
from src.shared.domain.criteria.filters import Filters


@dataclass
class Criteria:
    filters: Filters
    order: Order
    limit: int
    offset: int

    def has_filters(self) -> bool:
        return True if self.filters else False

    def has_order(self) -> bool:
        return True if self.order else None

    def plan_filters(self) -> list:
        return self.filters.filters

    def serialize(self) -> str:
        return f'{self.filters.serialize()}{self.order.serialize()}'