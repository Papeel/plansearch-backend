"""Query bus abstract class. """

from abc import ABC, abstractmethod
from typing import Awaitable

from src.shared.domain.bus.query.query import Query
from src.shared.domain.bus.query.response import Response


class QueryBus(ABC):
    @abstractmethod
    async def ask(self, query: Query) -> Awaitable[Response]: pass