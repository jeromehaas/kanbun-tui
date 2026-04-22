import os
from textual.screen import Screen
from textual.widgets import Label, Button, Input
from textual.containers import Grid
from app.api import LanesApi, ApiClient
from app.models import Board, Lane
from app.services import LanesService

# CLASS: CREATE LANE SCREEN
class CreateLaneScreen(Screen):

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
            Label("Create Lane", id="title"),
            Input(placeholder="First Name", id="input_lane_name"),
            Button("Cancel", variant="primary", id="cancel"),
            Button("OK",variant="primary" ,id="ok"), id="dialog"
        )

    # METHOD: BUTTON PRESSED EVENT
    async def on_button_pressed(self, event: Button.Pressed):

        # IF OK BUTTON
        if event.button.id == "ok":

            # GET LANE NAME
            lane_name = self.query_one("#input_lane_name", Input).value.strip()

            # DEFINE DATA
            data = Lane(
                name=lane_name,
            )

            # TRY-CATCH BLOCK
            try:

                # EXECUTE API CALL
                await self.lanes_service.create_lane(self.board, data)

            # HANDLE ERRORS
            except ApiError as error:

                # NOTIFY ABOUT ERROR
                self.notify(error.message, severity="error")
                return

            # UPDATE AND RELOAD SCREEN
            self.app.pop_screen()
            await self.app.screen.reload_screen()

        # IF CANCEL BUTTON
        if event.button.id == "cancel":

            # UPDATE AND RELOAD SCREEN
            self.app.pop_screen()
            await self.app.screen.reload_screen()
