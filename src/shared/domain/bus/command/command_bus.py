"""Command bus abstract class. """

from abc import ABC, abstractmethod
from typing import Awaitable

from src.shared.domain.bus.command.command import Command


class CommandBus(ABC):
    @abstractmethod
    async def dispatch(self, command: Command) -> Awaitable[None]: pass
