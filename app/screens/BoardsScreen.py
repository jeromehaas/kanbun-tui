# IMPORTS
import os
from dotenv import load_dotenv
from textual.app import ComposeResult
from textual.containers import Container
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import Header, Footer, Label, Log
from textual.binding import Binding
from app.api import ApiClient, BoardsApi, LanesApi, TasksApi, ApiError
from app.screens import (CreateLaneScreen, DeleteLaneScreen, EditLaneScreen, CreateBoardScreen, DeleteBoardScreen, EditBoardScreen, CreateTaskScreen)
from app.screens.DeleteTaskScreen import DeleteTaskScreen
from app.screens.EditTaskScreen import EditTaskScreen
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
        Binding("c", "create_board", "Create Board"),
        Binding("e", "edit_selected_board", "Edit Board"),
        Binding("d", "delete_selected_board", "Delete Board"),
        Binding("c", "create_lane", "Create Lane"),
        Binding("e", "edit_selected_lane", "Edit Lane"),
        Binding("d", "delete_selected_lane", "Delete Lane"),
        Binding("shift+left", "move_left_selected_lane", "Move Lane Left", priority=True),
        Binding("shift+right", "move_right_selected_lane", "Move Lane Right", priority=True),
        Binding("n", "create_task", "Create Task"),
        Binding("e", "edit_selected_task", "Edit Task"),
        Binding("d", "delete_selected_task", "Delete Task"),
        Binding("ctrl+left", "move_left_selected_task", "Move Task Left"),
        Binding("ctrl+right", "move_right_selected_task", "Move Task Right"),
    ]

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

        # RELOAD SCREEN
        await self.reload_screen()

    # METHOD: RELOAD ALL DATA IN SCREEN
    async def reload_screen(self) -> None:

        # GET SELECTED ELEMENTS
        selected_board_id = self.selected_board.id if self.selected_board else None
        selected_lane_id = self.selected_lane.id if self.selected_lane else None
        selected_task_id = self.selected_task.id if self.selected_task else None

        # FETCH AND UPDATE BOARDS
        await self.fetch_and_update_boards(selected_board_id)

        # FETCH AND UPDATE LANES
        await self.fetch_and_update_lanes(selected_lane_id, selected_task_id)

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
    async def fetch_and_update_boards(self, selected_board_id=None):

        # GET ALL BOARDS
        boards: list[Board] = await self.boards_service.get_all_boards()

        # GET BOARD WIDGET AND ASSIGN BOARDS TO IT
        boards_widget = self.query_one(BoardsContainerWidget)
        boards_widget.selected_board_id = selected_board_id
        boards_widget.boards = boards

        # KEEP SELECTED BOARD IF STILL AVAILABLE
        self.selected_board = next(
            (board for board in boards if board.id == selected_board_id),
            boards[0] if boards else None,
        )

    # METHOD: FETCH AND UPDATE LANES
    async def fetch_and_update_lanes(self, selected_lane_id=None, selected_task_id=None):

        # RESET IF NO BOARD IS SELECTED
        if self.selected_board is None:
            lanes_widget = self.query_one(LanesContainerWidget)
            lanes_widget.selected_lane_id = None
            lanes_widget.selected_task_id = None
            lanes_widget.lanes = []
            self.selected_lane = None
            self.selected_task = None
            return

        # GET ALL LANES
        lanes = await self.lanes_service.get_all_lanes(self.selected_board)

        # GET LANES WIDGET AND ASSIGN LANES TO IT
        lanes_widget = self.query_one(LanesContainerWidget)
        lanes_widget.selected_lane_id = selected_lane_id
        lanes_widget.selected_task_id = selected_task_id
        lanes_widget.lanes = lanes

        # KEEP SELECTED LANE IF STILL AVAILABLE
        self.selected_lane = next(
            (lane for lane in lanes if lane.id == selected_lane_id),
            lanes[0] if lanes else None,
        )

        # KEEP SELECTED TASK IF STILL AVAILABLE
        if self.selected_lane is None:
            self.selected_task = None
            return

        # KEEP SELECTED TASK IF STILL AVAILABLE
        self.selected_task = next(
            (task for task in self.selected_lane.tasks if task.id == selected_task_id),
            None,
        )

    # METHOD: CREATE A NEW BOARD
    def action_create_board(self):

        # DISPLAY CREATE BOARD SCREEN
        self.app.push_screen(CreateBoardScreen())
        self.refresh_bindings()

    # METHOD: DELETE THE SELECTED BOARD
    def action_delete_selected_board(self):

        # DISPLAY DELETE BOARD SCREEN
        self.app.push_screen(DeleteBoardScreen(self.selected_board))
        self.refresh_bindings()

    # METHOD: EDIT SELECTED BOARD
    def action_edit_selected_board(self):

        # DISPLAY EDIT BOARD SCREEN
        self.app.push_screen(EditBoardScreen(self.selected_board))
        self.refresh_bindings()

    # METHOD: CREATE LANE
    def action_create_lane(self):

        # DISPLAY CREATE LANE SCREEN
        self.app.push_screen(CreateLaneScreen(self.selected_board, self.selected_lane))
        self.refresh_bindings()

    # METHOD: EDIT SELECTED LANE
    def action_edit_selected_lane(self):

        # DISPLAY CREATE LANE SCREEN
        self.app.push_screen(EditLaneScreen(self.selected_board, self.selected_lane))
        self.refresh_bindings()

    # METHOD: MOVE SELECTED LANE LEFT
    async def action_move_left_selected_lane(self):

        # TRY-CATCH BLOCK
        try:

            # SET DIRECTION
            direction = "left"

            # MOVE LANE
            await self.lanes_service.move_lane(self.selected_board, self.selected_lane, direction)

        # HANDLE ERRORS
        except ApiError as error:

            # NOTIFY ABOUT ERROR
            self.notify(error.message, severity="error")
            return

        # UPDATE AND RELOAD SCREEN AND REFRESH BINDINGS
        await self.app.screen.reload_screen()
        self.refresh_bindings()

    # METHOD: MOVE SELECTED LANE RIGHT
    async def action_move_right_selected_lane(self):

        # TRY-CATCH BLOCK
        try:

            # SET DIRECTION
            direction = "right"

            # MOVE LANE
            await self.lanes_service.move_lane(self.selected_board, self.selected_lane, direction)

        # HANDLE ERRORS
        except ApiError as error:

            # NOTIFY ABOUT ERROR
            self.notify(error.message, severity="error")
            return

        # SHOW MODAL AND REFRESH BINDINGS
        await self.app.screen.reload_screen()
        self.refresh_bindings()

    # METHOD: DELETE SELECTED LANE
    def action_delete_selected_lane(self):

        # SHOW MODAL AND REFRESH BINDINGS
        self.app.push_screen(DeleteLaneScreen(self.selected_board, self.selected_lane))
        self.refresh_bindings()

    # METHOD: CREATE TASK
    def action_create_task(self):

        # SHOW MODAL AND REFRESH BINDINGS
        self.app.push_screen(CreateTaskScreen(self.selected_board, self.selected_lane))
        self.refresh_bindings()

    # METHOD: EDIT SELECTED TASK
    def action_edit_selected_task(self):

        # SHOW MODAL AND REFRESH BINDINGS
        self.app.push_screen(EditTaskScreen(self.selected_board, self.selected_lane, self.selected_task))
        self.refresh_bindings()

    # METHOD: DELETE SELECTED TASK
    def action_delete_selected_task(self):

        # SHOW MODAL AND REFRESH BINDINGS
        self.app.push_screen(DeleteTaskScreen(self.selected_board, self.selected_lane, self.selected_task))
        self.refresh_bindings()

    # METHOD: MOVE SELECTED TASK LEFT
    async def action_move_left_selected_task(self):

        # SHOW MODAL AND REFRESH BINDINGS
        self.tasks_service.move_task(self.selected_board, self.selected_lane, self.selected_task, self.lanes_service,"left")
        self.refresh_bindings()

    # METHOD: MOVE SELECTED TASK RIGHT
    async def action_move_right_selected_task(self):

        # SHOW MODAL AND REFRESH BINDINGS
        self.tasks_service.move_task(self.selected_board,  self.selected_lane, self.selected_task, self.lanes_service, "right")
        self.refresh_bindings()

    # METHOD CHECK ACTION
    def check_action(self, action: str, parameters: tuple[object, ...]) -> bool | None:

        # DEFINE BOARD BINDINGS
        if self.current_context == "board":
            return action in ("delete_selected_board", "rename_selected_board", "create_board", "edit_selected_board")

        # DEFINE LANE BINDINGS
        if self.current_context == "lane":
            return action in ("create_lane", "delete_selected_lane", "edit_selected_lane", "move_left_selected_lane", "move_right_selected_lane", "delete_selected_lane", "create_task")

        # DEFINE TASK BINDINGS
        if self.current_context == "task":
            return action in ("delete_selected_task","edit_selected_task","create_task","move_left_selected_task", "move_right_selected_task")
        return False
