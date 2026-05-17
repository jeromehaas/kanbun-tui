# IMPORTS
from app.api.TasksApi import TasksApi
from app.models.Board import Board
from app.models.Task import Task
from app.models.Lane import Lane
from app.services import LanesService

# CLASS: TASKS SERVICE
class TasksService:

    # METHOD: INIT
    def __init__(self, tasks_api: TasksApi):

        # SETUP FIELDS
        self.tasks_api = tasks_api

    # METHOD: GET ALL TASKS
    async def get_all_tasks(self) -> list[Task]:

        # GET ALL TASKS
        data = await self.tasks_api.get_tasks()

        # RETURN TASKS
        return [Task(
            board_id=item["board_id"],
            id=item["id"],
            title=item["title"])
            for item in data]

    # METHOD: CREATE TASK
    async def create_task(self, board: Board, lane: Lane, data: Task) -> Task:

        # CREATE TASK
        data = await self.tasks_api.create_task(board=board, lane=lane, task=data)

        # RETURN CREATED TASK
        return Task(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            position=data["position"],
        )

    # METHOD: EDIT TASK
    async def edit_task(self, board: Board, lane: Lane, task: Task) -> Task:

        # EDIT TASK
        data = await self.tasks_api.edit_task(board=board, lane=lane, task=task)

        # RETURN EDITED TASK
        return Task(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            position=data["position"],
        )

    # METHOD: DELETE TASK
    async def delete_task(self, board: Board, lane: Lane, task: Task) -> Task:

        # DELETE TASK
        data = await self.tasks_api.delete_task(board=board, lane=lane, task=task)

        # RETURN DELETED TASK
        return Task(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            position=data["position"],
        )

    # METHOD: MOVE TASK
    async def move_task(self, board: Board, lane: Lane, task: Task, lanes_service: LanesService, direction: str):

        # CALCULATE TARGET LANE POSITION
        target_lane_position = lane.position
        if direction == "right":
            target_lane_position = lane.position + 1
        if direction == "left":
            target_lane_position = lane.position - 1

        # GET ALL LANES IN CURRENT BOARD
        lanes = await lanes_service.get_all_lanes(board)

        # DISCOVER TARGET LANE
        target_lane: Lane = None
        for lane in lanes:
            if lane.position == target_lane_position:
                target_lane = lane
                break

        # ABORT IF NO TARGET LANE FOUND
        if target_lane is None:
            return

        # MOVE TASK VIA PATCH
        await self.tasks_api.move_task(board=board, lane=lane, task=task, target_lane=target_lane)
