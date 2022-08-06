from abc import ABC, abstractmethod

from src.shared.domain.aggregate import Aggregate


class MongoSchemaConverter(ABC):

    @staticmethod
    @abstractmethod
    def to_mongo(aggregate: Aggregate) -> dict: pass

    @staticmethod
    @abstractmethod
    def to_domain(primitives: dict) -> Aggregate: pass