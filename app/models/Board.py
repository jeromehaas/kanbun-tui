from dataclasses import dataclass, field
from app.models.Lane import Lane


# BOARD DATA CLASS
@dataclass
class Board:
    name: str
    id: int | None = None
    lanes: list[Lane] = field(default_factory=list)

