from dataclasses import dataclass, field
from .Task import Task

# BOARD DATA CLASS
@dataclass
class Lane:
    name: str
    id: int | None = None
    position: int | None = None
    tasks: list[Task] = field(default_factory=list)
