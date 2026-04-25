from app.api.TasksApi import TasksApi
from app.models.Board import Board
from app.models.Task import Task
from app.models.Lane import Lane

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

        # RETURN TAKS
        return [Task(
            board_id=item["board_id"],
            id=item["id"],
            title=item["title"])
            for item in data]

    async def create_task(self, board:Board, lane:Lane, data:Task) -> Task:

        # CREATE TASK
        data = await self.tasks_api.create_task(board=board, lane=lane, task=data)

        # RETURN CREATED TASK
        return Task(
            id=data["id"],
            title=data["title"],
            description=data["description"],
        )

    async def edit_task(self, board: Board, lane: Lane, task: Task) -> Task:
        # EDIT TASK
        data = await self.tasks_api.edit_task(board=board, lane=lane, task=task)

        # RETURN CREATED TASK
        return Task(
            id=data["id"],
            title=data["title"],
            description=data["description"],
        )
    async def delete_task(self, board: Board, lane: Lane, task: Task) -> Task:
        # EDIT TASK
        data = await self.tasks_api.delete_task(board=board, lane=lane, task=task)

        # RETURN DELETED TASK
        return Task(
            id=data["id"],
            title=data["title"],
            description=data["description"],
        )