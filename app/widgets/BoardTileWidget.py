from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container

# CLASS: BOARD TILE WIDGET
class BoardTileWidget(Container):

    # METHOD: INIT
    def __init__(self, board):

        # EXTEND CLASS
        super().__init__()

        # SETUP FIELDS
        self.board = board

    # METHOD: COMPOSE
    def compose(self) -> ComposeResult:

            # DISPLAY LABEL
            yield Label(self.board.name)
