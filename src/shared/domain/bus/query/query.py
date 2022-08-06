"""Query abstract class. """

from abc import ABC

from src.shared.domain.bus.dto import DTO


class Query(ABC, DTO):
    pass