from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container

from app.models.Board import Board


# BOARD TILE CLASS
class BoardTileWidget(Container):
    def __init__(self, board):
        super().__init__()
        self.board = board

    # BUILD WIDGET
    def compose(self) -> ComposeResult:
            yield Label(self.board.name)
