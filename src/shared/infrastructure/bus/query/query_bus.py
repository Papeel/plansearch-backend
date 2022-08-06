"""Query Bus. """
from typing import Awaitable, Optional

from src.shared.domain.bus.query.query import Query
from src.shared.domain.bus.query.response import Response
from src.shared.domain.bus.query.query_bus import QueryBus
from src.shared.domain.bus.query.query_handler import QueryHandler
from src.shared.infrastructure.bus.exceptions import QueryHandlerIsNotValidError, \
    QueryHandlerIsAlreadyRegisteredError, QueryHandlerIsNotRegisteredError


class InMemoryQueryBus(QueryBus):

    def __init__(self):
        self.__handlers: dict[str, QueryHandler] = {}

    def add_handler(self, handler: QueryHandler) -> None:
        if not issubclass(handler.__class__, QueryHandler):
            raise QueryHandlerIsNotValidError()
        query_name = handler.__class__.__name__.replace('Handler', '')
        if query_name in self.__handlers.keys():
            raise QueryHandlerIsAlreadyRegisteredError()
        self.__handlers[query_name] = handler

    async def ask(self, query: Query) -> Awaitable[Optional[Response]]:
        query_name = query.__class__.__name__
        if query_name not in self.__handlers.keys():
            raise QueryHandlerIsNotRegisteredError()
        query_handler = self.__handlers.get(query.__class__.__name__)
        return await query_handler(query)