"""CommandBus and QueryBus exceptions. """


class CommandHandlerIsNotValidError(Exception): pass


class CommandHandlerIsNotRegisteredError(Exception): pass


class CommandHandlerIsAlreadyRegisteredError(Exception): pass


class QueryHandlerIsNotValidError(Exception): pass


class QueryHandlerIsNotRegisteredError(Exception): pass


class QueryHandlerIsAlreadyRegisteredError(Exception): pass