"""Query handler abstract class. """

from abc import ABC, abstractmethod
from typing import Awaitable

from src.shared.domain.bus.query.query import Query
from src.shared.domain.bus.query.response import Response

class QueryHandler(ABC):
    @abstractmethod
    async def __call__(self, query: Query, *args, **kwargs) -> Awaitable[Response]: pass