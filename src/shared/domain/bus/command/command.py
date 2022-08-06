"""Command abstract class. """

from abc import ABC

from src.shared.domain.bus.dto import DTO


class Command(ABC, DTO):
    pass