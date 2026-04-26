# IMPORTS
import os
from textual.screen import Screen
from textual.widgets import Label, Button
from textual.containers import Grid
from app.api.ApiClient import ApiClient
from app.api.BoardsApi import BoardsApi
from app.models.Board import Board

# SCREEN CLASS FOR DELETE A BOARD
class DeleteBoardScreen(Screen):

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
            Label("Delete board", id="title"),
            Label(f"Do you want to delete the board '{self.board.name}'?", id="question"),
            Button("Cancel", variant="primary", id="cancel"),
            Button("OK", variant="primary", id="ok"),
        id="dialog")

    # METHOD: BUTTON PRESSED EVENT
    async def on_button_pressed(self, event: Button.Pressed):

        # IF OK BUTTON
        if event.button.id == "ok":

            # DELETE BOARD
            await self.boards_api.delete_board_by_id(self.board.id)

            # CLOSE SCREEN AND REFRESH
            self.app.pop_screen()
            await self.app.screen.reload_screen()

        # IF CANCEL BUTTON
        if event.button.id == "cancel":

            # CLOSE SCREEN AND REFRESH
            self.app.pop_screen()
            await self.app.screen.reload_screen()
