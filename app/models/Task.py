from dataclasses import dataclass

# TASK DATA CLASS
@dataclass
class Task:
    board_id: int
    id: int
    title: str