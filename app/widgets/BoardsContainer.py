from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container
from app.widgets.BoardTile import BoardTile


# BOARDS CONTAINER CLASS
class BoardsContainer(Container):


    def compose(self) -> ComposeResult:
            yield Label("Boards")
            yield BoardTile()

