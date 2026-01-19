from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum
import itertools


id_generator = itertools.count(1)


class Status(StrEnum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


@dataclass
class Task:
    """
    The class create a task in T0DO list
    """

    id: int = field(default_factory=lambda: next(id_generator))
    title: str = "Untitled Task"
    description: str = ""
    status: Status = Status.TODO
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime | None = None

    def mark_updated(self) -> None:
        """Update the modification timestamp to the current time."""
        self.updated_at = datetime.now()

    def __post_init__(self) -> None:
        """Clean up input data after the object is initialized."""
        self.title = self.title.strip()
        self.description = self.description.strip()

        if isinstance(self.status, str):
            self.status = Status(self.status)
        elif not isinstance(self.status, Status):
            raise ValueError("status must be Status enum")
