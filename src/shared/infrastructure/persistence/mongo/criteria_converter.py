"""MongoCriteriaConverter. """

from dataclasses import dataclass
from distutils.util import strtobool
from typing import final
from uuid import UUID

import pymongo

from src.shared.domain.criteria.criteria import Criteria
from src.shared.domain.utils import Utils


@final
@dataclass
class MongoCriteriaConverter:
    criteria: Criteria

    def __post_init__(self):
        self.filters = self.filter_builder()
        self.limit = self.criteria.limit
        self.offset = self.criteria.offset
        self.order_by = self.criteria.order.order_by.value
        self.order_type = self.order_type_builder()

    def filter_builder(self):
        filters = {}
        for filter in self.criteria.filters.filters:
            field = filter.field.value
            value = filter.value.value
            if field.lower() in {'_id', 'id', 'ids'}:
                filters['_id'] = {'$in' : [UUID(x) for x in value.split(',') ]}
                continue
            if Utils.is_valid_uuid(value):
                filters[field] = UUID(value)
                continue
            if field.lower() in {'user_id', 'user_ids', 'users_ids'}:
                filters['user_id'] = {'$in': [str(x) for x in value]}
                continue
            if value.lower() == 'true' or value.lower() == 'false':
                filters[field] = bool(strtobool(value))
                continue
            if value.isdigit():
                filters[field] = int(value)
                continue
            if value.replace('.', '').isdigit():
                filters[field] = float(value)
                continue
            filters[field] = value
        return filters

    def order_type_builder(self):
        order_type = self.criteria.order.order_type.value
        if order_type.lower() == 'asc':
            return pymongo.ASCENDING
        if order_type.lower() == 'desc':
            return pymongo.DESCENDING