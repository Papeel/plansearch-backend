"""OrderType. """

from enum import Enum


class OrderType(Enum):
    ASC = 'asc'
    DESC = 'desc'
    NONE = 'none'