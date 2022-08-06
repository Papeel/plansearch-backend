"""ValueObject. """

from abc import abstractmethod

from src.shared.domain.null import Null


class ValueObject:

    def __post_init__(self):
        self.__call_ensures()

    @abstractmethod
    def value(self) -> str:
        pass

    @abstractmethod
    def _ensure_type(self) -> None:
        pass

    def __new__(cls, value=None):
        if isinstance(value, Null): return value
        return object.__new__(cls)

    def __call_ensures(self):
        methods = dir(self)
        getattr(self, '_ensure_type')()
        methods.remove('_ensure_type')
        for method in methods:
            if method.startswith('_ensure'):
                getattr(self, method)()

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, type(self)): return False
        return self.value == __o.value

    def __hash__(self) -> int:
        return hash(self.value)