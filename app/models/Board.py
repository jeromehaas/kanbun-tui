from dataclasses import dataclass

# BOARD DATA CLASS
@dataclass
class Board:
    id: int
    name: str
    lanes: list[dict]