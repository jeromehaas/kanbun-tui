# IMOPRTS
import os
from textual.screen import Screen
from textual.widgets import Label, Button, Input
from textual.containers import Grid
from app.api.ApiClient import ApiClient
from app.api.BoardsApi import BoardsApi
from app.models.Board import Board

# SCREEN CLASS FOR EDIT A BOARD
class EditBoardScreen(Screen):

    # METHOD: INIT
    def __init__(self, board: Board = None):

        # GET PARENT
        super().__init__()

        # GET BOARD
        self.board = board

        # CREATE CLIENT
        api_client = ApiClient(
            base_url=os.getenv("API_BASE_URL"),
            token=os.getenv("API_TOKEN"),
        )

        # CREATE SERVICES
        self.boards_api = BoardsApi(api_client)

    # COMPOSE ALL ELEMENTS
    def compose(self):

        # DEFINE CONTENT
        yield Grid(
            Label("Edit Board", id="title"),
            Input(value=self.board.name, type="text", id="input_board_name"),
            Button("Cancel", variant="primary", id="cancel"),
            Button("OK", variant="primary", id="ok"), id="dialog"
        )

    # METHOD: BUTTON PRESSED EVENT
    async def on_button_pressed(self, event: Button.Pressed):

        # IF OK BUTTON
        if event.button.id == "ok":

            # GET VALUE FROM INPUT
            self.board.name = self.query_one("#input_board_name", Input).value

            # PATCH DATA
            await self.boards_api.edit_board_by_id(self.board)

            # CLOSE SCREEN AND REFRESH
            self.app.pop_screen()
            await self.app.screen.reload_screen()

        # IF CANCEL BUTTON
        if event.button.id == "cancel":

            # CLOSE SCREEN AND REFRESH
            self.app.pop_screen()
            await self.app.screen.reload_screen()
