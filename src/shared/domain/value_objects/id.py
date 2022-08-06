"""Id. """
from dataclasses import dataclass, field
from uuid import UUID, uuid4

from src.shared.domain.exceptions import IdIsNotAStrInstanceError, IdHasNotAValidFormatError
from src.shared.domain.value_object import ValueObject


@dataclass(frozen=True)
class Uuid(ValueObject):
    value: str = field(default_factory=lambda: str(uuid4()))

    def _ensure_type(self):
        if not isinstance(self.value, str):
            raise IdIsNotAStrInstanceError()

    def _ensure_is_valid_id(self) -> None:
        try:
            UUID(self.value, version=4)
        except ValueError:
            raise IdHasNotAValidFormatError()