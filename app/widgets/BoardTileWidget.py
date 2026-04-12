from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container

# BOARD TILE CLASS
class BoardTileWidget(Container):

    # BUILD WIDGET
    def compose(self) -> ComposeResult:
            yield Label("BoardName")
