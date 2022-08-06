"""DomainEvent. """

from abc import ABC, abstractmethod
import uuid
from datetime import datetime
from dataclasses import dataclass, asdict

@dataclass
class DomainEvent(ABC):

    def __post_init__(self):
        self.__event_id = getattr(self, 'event_id', str(uuid.uuid4()))
        self.__occurred_on = getattr(self, 'occurred_on', datetime.utcnow().timestamp())

    @abstractmethod
    def event_name(self) -> str: pass

    @property
    def aggregate_id(self) -> str:
        return getattr(self, 'id', None)

    @property
    def event_id(self) -> str:
        return self.__event_id

    @property
    def event_meta(self) -> dict:
        return getattr(self, 'meta', dict())

    @property
    def occurred_on(self) -> float:
        return self.__occurred_on

    def to_primitives(self) -> dict:
        primitives = asdict(self)
        if primitives.get('id'): primitives.pop('id')
        if primitives.get('meta'): primitives.pop('meta')
        if primitives.get('event_id'): primitives.pop('event_id')
        if primitives.get('occurred_on'): primitives.pop('occurred_on')
        return primitives
    