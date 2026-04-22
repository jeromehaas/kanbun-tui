import os
from textual.screen import Screen
from textual.widgets import Label, Button
from textual.containers import Grid
from app.api import LanesApi, ApiClient
from app.models import Board, Lane
from app.services import LanesService

# CLASS: DELETE LANE SCREEN
class DeleteLaneScreen(Screen):

    # METHOD: INIT
    def __init__(self, board: Board=None, lane: Lane=None):

        # GET PARENT
        super().__init__()

        # ASSIGN PROPERTIES
        self.board: Board = board
        self.lane: Lane = lane

        # CREATE CLIENT
        api_client = ApiClient(
            base_url=os.getenv("API_BASE_URL"),
            token=os.getenv("API_TOKEN"),
        )

        # SETUP SERVICES
        self.lanes_service = LanesService(LanesApi(api_client))

    # COMPOSE ALL ELEMENTS
    def compose(self):
        yield Grid(
            Label("Delete Lane", id="title"),
            Label(f"Do you want to delete the lane '{self.lane.name}'?", id="question"),
            Button("Cancel", variant="primary", id="cancel"),
            Button("OK",variant="primary" ,id="ok"), id="dialog"
        )

    # METHOD: BUTTON PRESSED EVENT
    async def on_button_pressed(self, event: Button.Pressed):

        # IF OK BUTTON
        if event.button.id == "ok":

            # TRY-CATCH BLOCK
            try:

                # GET LANE NAME
                await self.lanes_service.delete_lane(self.board, self.lane)

            # HANDLE ERRORS
            except ApiError as error:

                # NOTIFY ABOUT ERROR
                self.notify(error.message, severity="error")

            # UPDATE AND RELOAD SCREEN
            self.app.pop_screen()
            await self.app.screen.reload_screen()

        # IF CANCEL BUTTON
        if event.button.id == "cancel":

            # UPDATE AND RELOAD SCREEN
            self.app.pop_screen()
            await self.app.screen.reload_screen()
