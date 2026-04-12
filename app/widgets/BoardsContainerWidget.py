from textual.app import ComposeResult
from textual.widgets import Label, ListItem, ListView
from textual.containers import Container
from app.widgets.BoardTileWidget import BoardTileWidget
from textual.reactive import reactive
from textual.message import Message

# BOARDS CONTAINER WIDGET CLASS
class BoardsContainerWidget(Container):

    boards = reactive([], recompose=True)

    class BoardSelected(Message):
        def __init__(self, board):
            self.board = board
            super().__init__()

    # BUILD WIDGET
    def compose(self) -> ComposeResult:
            yield Label("Boards")

            if not self.boards:
                yield Label("Keine Boards gefunden")
                return

            with ListView():
                for board in self.boards:
                    yield ListItem(BoardTileWidget(board))

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        selected_item = event.item

        # Das eigentliche Board aus dem ListItem holen
        board_tile = selected_item.query_one(BoardTileWidget)
        board = board_tile.board

        # Eigene Message an Parent senden
        self.post_message(self.BoardSelected(board))