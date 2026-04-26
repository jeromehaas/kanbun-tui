# IMPORTS
from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container

# CLASS: BOARD TILE WIDGET
class BoardTileWidget(Container):
    MAXIMUM_NUMBER_OF_DIGITS = 44

    # METHOD: INIT
    def __init__(self, board):

        # EXTEND CLASS
        super().__init__()

        # SETUP FIELDS
        self.board = board

    # METHOD: COMPOSE
    def compose(self) -> ComposeResult:

        # SHORTEN NAME IF TO LONG
        if len(self.board.name) > self.MAXIMUM_NUMBER_OF_DIGITS:
            name = str(self.board.name[:self.MAXIMUM_NUMBER_OF_DIGITS]) + "..."
        else:
            name = str(self.board.name)

        # DISPLAY LABEL
        yield Label(name)
