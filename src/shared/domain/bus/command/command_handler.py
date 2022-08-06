"""Command handler abstract class. """

from abc import ABC, abstractmethod

from src.shared.domain.bus.command.command import Command


class CommandHandler(ABC):
    @abstractmethod
    async def __call__(self, command: Command, *args, **kwargs) -> None: pass