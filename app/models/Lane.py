from dataclasses import dataclass
from .Task import Task

# BOARD DATA CLASS
@dataclass
class Lane:
    id: int
    name: str
    position: int
    tasks: list[Task]
