from textual.app import ComposeResult
from textual.widgets import Label, ListItem, ListView
from textual.containers import Container
from app.widgets.BoardTileWidget import BoardTileWidget
from textual.reactive import reactive


# BOARDS CONTAINER WIDGET CLASS
class BoardsContainerWidget(Container):

    boards = reactive([], recompose=True)

    # BUILD WIDGET
    def compose(self) -> ComposeResult:
            yield Label("Boards")

            if not self.boards:
                yield Label("Keine Boards gefunden")
                return

            with ListView():
                for board in self.boards:
                    yield ListItem(BoardTileWidget(board))

