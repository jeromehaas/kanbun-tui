from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container
from app.widgets.BoardTileWidget import BoardTileWidget


# BOARDS CONTAINER WIDGET CLASS
class BoardsContainerWidget(Container):

    # BUILD WIDGET
    def compose(self) -> ComposeResult:
            yield Label("Boards")
            yield BoardTileWidget()

