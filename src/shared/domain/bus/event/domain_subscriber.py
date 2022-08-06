"""DomainSubscribed abstract class. """

from abc import abstractmethod
from typing import List


class DomainEventSubscriber:
    @staticmethod
    @abstractmethod
    def subscribed_to() -> List[str]: pass