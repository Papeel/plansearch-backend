"""Order. """

from typing import final
from dataclasses import dataclass

from src.shared.domain.criteria.order_by import OrderBy
from src.shared.domain.criteria.order_type import OrderType


@final
@dataclass
class Order:
    order_by: OrderBy
    order_type: OrderType

    @classmethod
    def from_values(cls, order_by: str, order: str):
        return cls.none() if order_by is None else cls(OrderBy(order_by), OrderType(order))

    @classmethod
    def none(cls):
        return cls(OrderBy(''), OrderType('none'))

    def serialize(self) -> str:
        return f'{self.order_by.value}{self.order_type.value}'