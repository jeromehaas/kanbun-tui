from dataclasses import dataclass
from app.models.Lane import Lane


# BOARD DATA CLASS
@dataclass
class Board:
    id: int
    name: str
    lanes: list[Lane]