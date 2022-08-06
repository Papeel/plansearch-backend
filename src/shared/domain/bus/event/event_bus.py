"""EventBus. """

from abc import ABC, abstractmethod
from typing import List

from src.shared.domain.bus.event.domain_event import DomainEvent


class EventBus(ABC):
    @abstractmethod
    async def publish(self, events: List[DomainEvent]) -> None: pass