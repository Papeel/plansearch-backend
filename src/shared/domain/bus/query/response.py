
"""Response. """

from abc import ABC, abstractmethod


class Response(ABC):
    @abstractmethod
    async def to_primitives(self): pass