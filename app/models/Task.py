# IMPORTS
from dataclasses import dataclass, field

# TASK DATA CLASS
@dataclass
class Task:
    title: str
    description: str
    id: int = None
    position: int = 0
    