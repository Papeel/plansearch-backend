from dataclasses import dataclass

from src.shared.domain.bus.query.query import Query


@dataclass(frozen=True)
class CriteriaQuery(Query):
    filters: dict[str, str]
    order_by: str
    order: str
    limit: int
    offset: int

    @classmethod
    def from_primitives(cls, default_filters=True, **kwargs):
        order_by = kwargs.pop('order_by', 'created_at')
        order = kwargs.pop('order', 'desc')
        limit = kwargs.pop('limit', 10)
        offset = kwargs.pop('offset', 0)
        filters = kwargs if kwargs else {'active': 'true'} if default_filters else None
        return cls(filters, order_by, order, int(limit), int(offset))