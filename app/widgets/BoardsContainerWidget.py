from textual.app import ComposeResult
from textual.widgets import Label, ListItem, ListView
from textual.containers import Container
from app.widgets.BoardTileWidget import BoardTileWidget
from textual.reactive import reactive
from textual.message import Message

# BOARDS CONTAINER WIDGET CLASS
class BoardsContainerWidget(Container):

    # DEFINE BOARDS
    boards = reactive([], recompose=True)

    # CLASS: BOARDS SELECTED
    class BoardSelected(Message):

        # METHOD: INIT
        def __init__(self, board):

            # EXTEND CLASS
            super().__init__()

            # SETUP FIELDS
            self.board = board


    # METHOD: COMPOSE
    def compose(self) -> ComposeResult:

            # SETUP FIELDS
            yield Label("Boards")

            # CHECK FOR BOARDS
            if not self.boards:
                yield Label("Keine Boards gefunden")
                return

            # SETUP LIST VIEW
            with ListView():
                for board in self.boards:
                    yield ListItem(BoardTileWidget(board))

    # HOOK: ON LIST VIEW SELECTED
    def on_list_view_selected(self, event: ListView.Selected) -> None:

        # GET SELECTED ITEM
        selected_item = event.item

        # GET BOARD TILE and BOARD
        board_tile = selected_item.query_one(BoardTileWidget)
        board = board_tile.board

        # DISPATCH SELECTED BOARD
        self.post_message(self.BoardSelected(board))

    # HOOK: ON LIST VIEW SELECTED
    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:

        # GET SELECTED ITEM
        selected_item = event.item

        # GET BOARD TILE and BOARD
        board_tile = selected_item.query_one(BoardTileWidget)
        board = board_tile.board

        # DISPATCH SELECTED BOARD
        self.post_message(self.BoardSelected(board))