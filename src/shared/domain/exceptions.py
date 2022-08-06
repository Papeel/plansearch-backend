"""Shared domain exceptions. """
from dataclasses import dataclass


APP = 'shared'
CODE_PREFIX = 'SH'


class DomainException(Exception):
    """Common base class for all domain exceptions. """

    def __init_subclass__(cls, app: str = None, status: int = None, code: str = None, detail: str = None,
                          message: str = None):
        super().__init_subclass__()
        cls.app = app
        cls.status = status
        cls.code = code
        cls.detail = detail
        cls.message = message

    def __init__(self, **kwargs: object) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)


@dataclass
class DtoPropertyCanNotBeEmptyError(DomainException):
    message: str
    detail: str = 'invalid_dto_property'
    code: str = 'ACD339C'
    status: int = 422


@dataclass
class DtoUnacceptedPropertyError(DomainException):
    message: str
    detail: str = 'unaccepted_attribute'
    code: str = '7EF931B'
    status: int = 422


@dataclass
class DtoRequiredPropertyError(DomainException):
    message: str
    detail: str = 'required_attribute'
    code: str = '658C15F'
    status = 400

    
class IdIsNotAStrInstanceError(
    DomainException,
    app=APP,
    status=422,
    code='1F297',
    detail='invalid_id',
    message='Id is not a string'): pass


class IdHasNotAValidFormatError(
    DomainException,
    app=APP,
    status=422,
    code=f'{CODE_PREFIX}EB4E1',
    detail='invalid_id',
    message='Id has not a valid format (UUID)'): pass
