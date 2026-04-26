# IMPORTS
from dataclasses import dataclass

# TASK DATA CLASS
@dataclass
class Task:
    title: str
    description: str
    id: int = None
    