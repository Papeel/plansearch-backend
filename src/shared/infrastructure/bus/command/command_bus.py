"""Command Bus. """

from src.shared.domain.bus.command.command import Command
from src.shared.domain.bus.command.command_bus import CommandBus
from src.shared.domain.bus.command.command_handler import CommandHandler
from src.shared.infrastructure.bus.exceptions import CommandHandlerIsNotValidError, \
    CommandHandlerIsAlreadyRegisteredError, CommandHandlerIsNotRegisteredError


class InMemoryCommandBus(CommandBus):

    def __init__(self):
        self.__handlers: dict[str, CommandHandler] = {}

    def add_handler(self, handler: CommandHandler) -> None:
        if not issubclass(handler.__class__, CommandHandler):
            raise CommandHandlerIsNotValidError()
        command_name = handler.__class__.__name__.replace('Handler', '')
        if command_name in self.__handlers.keys():
            raise CommandHandlerIsAlreadyRegisteredError()
        self.__handlers[command_name] = handler

    async def dispatch(self, command: Command) -> None:
        command_name = command.__class__.__name__
        if command_name not in self.__handlers.keys():
            raise CommandHandlerIsNotRegisteredError()
        command_handler = self.__handlers.get(command.__class__.__name__)
        await command_handler(command)