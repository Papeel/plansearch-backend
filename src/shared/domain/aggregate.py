"""Aggregate. """

from abc import ABC
from typing import List

from src.shared.domain.bus.event.domain_event import DomainEvent
from src.shared.domain.null import Null


class Aggregate(ABC):

    def __init__(self):
        self.domain_events = None

    def __post_init__(self):
        self.__call_ensures()
        object.__setattr__(self, "domain_events", [])

    def __call_ensures(self):
        for method in dir(self):
            if method.startswith('_ensure'):
                getattr(self, method)()

    def pull_event(self) -> List[DomainEvent]:
        domain_events = self.domain_events.copy()
        self.domain_events.clear()
        return domain_events

    def record_event(self, event: DomainEvent) -> None:
        self.domain_events.append(event)

    def update(self, locals):
        changed = []
        for k, v in locals.items():
            if k == 'self' or k == 'meta': continue
            if isinstance(v, Null) or (isinstance(v, list) and len(v) and isinstance(v[0], Null)): continue
            if v != getattr(self, k):
                setattr(self, k, v)
                changed.append(k)

        return changed