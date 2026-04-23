import os
from dotenv import load_dotenv
from textual.app import ComposeResult
from textual.containers import Container
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import Header, Footer, Label, Log
from textual.binding import Binding
from app.api import ApiClient, BoardsApi, LanesApi, TasksApi
from app.screens import (CreateLaneScreen, DeleteBoardScreen, DeleteLaneScreen, EditLaneScreen, MoveLeftLaneScreen, MoveRightLaneScreen)
from app.services import BoardsService, LanesService, TasksService
from app.widgets import BoardsContainerWidget, LaneWidget, LanesContainerWidget
from app.models import Board

# CLASS: BOARDS SCREEN
class BoardsScreen(Screen):

    # DEFINE SELECTED ELEMENTS
    selected_board = reactive(None)
    selected_lane = reactive(None)
    selected_task = reactive(None)
    current_context = reactive("default")

    # KEY BINDINGS
    BINDINGS = [
        Binding("d", "delete_selected_board", "Delete Board"),
        Binding("r", "rename_selected_board", "Rename Board"),
        Binding("c", "create_lane", "Create Lane"),
        Binding("d", "delete_selected_lane", "Delete Lane"),
        Binding("left", "move_left_selected_lane", "Move Lane Left", priority=True),
        Binding("right", "move_right_selected_lane", "Move Lane Right", priority=True),
        Binding("e", "edit_selected_lane", "Edit Lane"),

    ]    # METHOD: INIT
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

        # SETUP API
        self.lanes_api = LanesApi(api_client)

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

    # HOOK: ON TASKS SELECTED
    def on_lane_widget_task_selected(self, event: LaneWidget.TaskSelected) -> None:

        # GET TASK
        task = event.task

        # UPDATE STATE
        self.selected_task = task
        self.current_context = "task"

        # UPDATE BINDINGS
        self.refresh_bindings()

    # HOOK: ON BOARDS CONTAINER WIDGET BOARD SELECTED
    async def on_boards_container_widget_board_selected(self, event: BoardsContainerWidget.BoardSelected) -> None:

        # GET BOARD FROM EVENT
        board = event.board

        # UPDATE SELECTED BOARD
        self.selected_board = board
        self.current_context = "board"

        # REFRESH BINDINGS
        self.refresh_bindings()

        # FETCH AND UPDATE LANES
        await self.fetch_and_update_lanes()

    # HOOK ON LANE SELECTED
    def on_lane_widget_lane_selected(self, event: LaneWidget.LaneSelected) -> None:

        # GET LANE
        lane = event.lane

        # UPDATE STATE
        self.selected_lane = lane
        self.current_context = "lane"

        # REFRESH BINDINGS
        self.refresh_bindings()

    # METHOD: FETCH AND UPDATE BOARDS
    async def fetch_and_update_boards(self):

        # GET ALL BOARDS
        boards: list[Board] = await self.boards_service.get_all_boards()

        # GET BOARD WIDGET AND ASSIGN BOARDS TO IT
        boards_widget = self.query_one(BoardsContainerWidget)
        boards_widget.boards = boards

        # UPDATE SELECTED BOARDS WITH FIRST ENTRY
        if boards:
            self.selected_board = boards[0]
        else:
            self.selected_board = []

    # METHOD: FETCH AND UPDATE LANES
    async def fetch_and_update_lanes(self):

        # GET ALL LANES
        lanes = await self.lanes_service.get_all_lanes(self.selected_board)

        # GET LANES WIDGET AND ASSIGN LANES TO IT
        lanes_widget = self.query_one(LanesContainerWidget)
        lanes_widget.lanes = lanes

    # METHOD: DELETE THE SELECTED BOARD
    def action_delete_selected_board(self):

        # DISPLAY DELETE SCREEN
        self.app.push_screen(DeleteBoardScreen(self.selected_board))
        self.refresh_bindings()

    # METHOD: DELETE THE SELECTED BOARD
    def action_rename_selected_board(self):

        # RENAME SCREEN
        self.notify(str('ACTION: RENAME SELECTED BOARD'))

    # METHOD: CREATE LANE
    def action_create_lane(self):

        # NOTIFY
        self.app.push_screen(CreateLaneScreen(self.selected_board, self.selected_lane))

        # REFRESH BINDINGS
        self.refresh_bindings()

    # METHOD: CREATE LANE
    def action_edit_selected_lane(self):

        # SHOW MODAL
        self.app.push_screen(EditLaneScreen(self.selected_board, self.selected_lane))

        # REFRESH BINDINGS
        self.refresh_bindings()

    # METHOD: CREATE LANE
    def action_move_left_selected_lane(self):

        # SHOW MODAL
        self.app.push_screen(MoveLeftLaneScreen(self.selected_board, self.selected_lane))

        # REFRESH BINDINGS
        self.refresh_bindings()

    # METHOD: CREATE LANE
    def action_move_right_selected_lane(self):

        # SHOW MODAL
        self.app.push_screen(MoveRightLaneScreen(self.selected_board, self.selected_lane))

        # REFRESH BINDINGS
        self.refresh_bindings()

    # METHOD: CREATE LANE
    def action_delete_selected_lane(self):

        # SHOW MODAL
        self.app.push_screen(DeleteLaneScreen(self.selected_board, self.selected_lane))

        # REFRESH BINDINGS
        self.refresh_bindings()

    def check_action(self, action: str, parameters: tuple[object, ...]) -> bool | None:
        if self.current_context == "board":
            return action in ("delete_selected_board", "rename_selected_board")
        if self.current_context == "lane":
            return action in ("create_lane", "delete_selected_lane", "edit_selected_lane", "move_left_selected_lane", "move_right_selected_lane", "delete_selected_lane")
        if self.current_context == "task":
            return action in ("delete_selected_task",)
        return False
