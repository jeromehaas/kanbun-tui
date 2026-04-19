import os
from dotenv import load_dotenv
from textual.app import ComposeResult
from textual.containers import Container
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import Header, Footer, Label, Log
from app.api.ApiClient import ApiClient
from app.api.BoardsApi import BoardsApi
from app.api.TasksApi import TasksApi
from app.api.LanesApi import LanesApi
from app.screens.DeleteBoardScreen import DeleteBoardScreen
from app.services.BoardsService import BoardsService
from app.services.TasksService import TasksService
from app.services.LanesService import LanesService
from app.widgets.BoardsContainerWidget import BoardsContainerWidget
from app.widgets.LaneWidget import LaneWidget
from app.widgets.LanesContainerWidget import LanesContainerWidget
from app.models.Board import Board

# CLASS: BOARDS SCREEN
class BoardsScreen(Screen):

    # DEFINE SELECTED ELEMENTS
    selected_board = reactive(None)

    selected_lane_id = reactive("")

    selected_task_id = reactive("")

    # KEY BINDINGS
    BINDINGS = [("ctrl+d", "delete_selected_element", "Delete")]

    # METHOD: INIT
    def __init__(self):

        # EXTEND SUPER CLASS
        super().__init__()

        # LOAD SECRETS
        load_dotenv()

        # CREATE CLIENT
        api_client = ApiClient(
            base_url=os.getenv("API_BASE_URL"),
            token=os.getenv("API_TOKEN"),
        )

        # CREATE SERVICES
        self.tasks_service = TasksService(TasksApi(api_client))
        self.boards_service = BoardsService(BoardsApi(api_client))
        self.lanes_service = LanesService(LanesApi(api_client))

    # METHOD: COMPOSE
    def compose(self) -> ComposeResult:

        # DISPLAY CONTAINER AND CONTENTS
        with Container(id="main-area"):
            yield Header()
            yield BoardsContainerWidget()
            yield LanesContainerWidget()
            yield Label("", id="selected-board")
            yield Footer()

    # HOOK: ON MOUNT
    async def on_mount(self) -> None:
        await self.reload_screen()

    # METHOD: RELOAD ALL DATA IN SCREEN
    async def reload_screen(self) -> None:

        # FETCH AND UPDATE BOARDS
        await self.fetch_and_update_boards()

        # FETCH AND UPDATE LANES
        await self.fetch_and_update_lanes()


    # HOOK: ON BOARDS CONTAINER WIDGET BOARD SELECTED
    async def on_boards_container_widget_board_selected(self, event: BoardsContainerWidget.BoardSelected) -> None:

        # GET BOARD FROM EVENT
        board = event.board

        # UPDATE SELECTED BOARD
        self.selected_board_id = str(board.id)
        self.selected_board = board

        # FETCH AND UPDATE LANES
        await self.fetch_and_update_lanes()

    # HOOK ON LANE SELECTED
    def on_lane_widget_lane_selected(self, event: LaneWidget.LaneSelected) -> None:
        lane_id = event.lane
        self.notify(f"Event Lane: {str(lane_id)}")

    # METHOD: FETCH AND UPDATE BOARDS
    async def fetch_and_update_boards(self):

        # GET ALL BOARDS
        boards: list[Board] = await self.boards_service.get_all_boards()

        # GET BOARD WIDGET AND ASSIGN BOARDS TO IT
        boards_widget = self.query_one(BoardsContainerWidget)
        boards_widget.boards = boards

        # UPDATE SELECTED BOARDS WITH FIRST ENTRY
        if boards:
            self.selected_board_id = str(boards[0].id)
            self.selected_board = boards[0]
        else:
            self.selected_board_id = ""
            self.selected_board = []

    # METHOD: FETCH AND UPDATE LANES
    async def fetch_and_update_lanes(self):

        # GET ALL LANES
        lanes = await self.lanes_service.get_all_lanes(self.selected_board_id)

        # GET LANES WIDGET AND ASSIGN LANES TO IT
        lanes_widget = self.query_one(LanesContainerWidget)
        lanes_widget.lanes = lanes

    # METHOD: DELETE A SELECTED ITEM
    def action_delete_selected_element(self):

        # DISPLAY DELETE SCREEN
        self.app.push_screen(DeleteBoardScreen(self.selected_board))
