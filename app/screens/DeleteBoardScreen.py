import os
from textual.screen import ModalScreen, Screen
from textual.widgets import Label, Button
from textual.containers import Container, Grid
from app.api.ApiClient import ApiClient
from app.api.BoardsApi import BoardsApi
from app.services.BoardsService import BoardsService


# SCREEN CLASS FOR DELETE A BOARD
class DeleteBoardScreen(Screen):

    def __init__(self, board_id=None):
        super().__init__()
        self.board_name = None
        self.board_id = board_id

        # CREATE CLIENT
        api_client = ApiClient(
            base_url=os.getenv("API_BASE_URL"),
            token=os.getenv("API_TOKEN"),
        )

        # CREATE SERVICES
        self.boards_api = BoardsApi(api_client)

    def compose(self):
        yield Grid(
    Label("Delete Board", id="title"),
             Label(f"Do you want to delete the board {self.board_name}?", id="question"),
            Button("Cancel", variant="primary", id="cancel"),
             Button("OK",variant="primary" ,id="delete"), id="dialog"
        )

    async def on_button_pressed(self, event: Button.Pressed):

        if event.button.id == "delete":
            await self.boards_api.delete_board_by_id(self.board_id)
            self.app.pop_screen()
            await self.app.screen.reload_screen()

        if event.button.id == "cancel":
            self.app.pop_screen()
            await self.app.screen.reload_screen()