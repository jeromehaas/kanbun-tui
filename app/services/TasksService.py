from app.api.TasksApi import TasksApi
from app.models.Task import Task

# WRITES TASK-DATA TO MODEL
class TasksService:
    def __init__(self, tasks_api: TasksApi):
        self.tasks_api = tasks_api

    # GET ALL TASKS
    async def get_all_tasks(self) -> list[Task]:
        data = await self.tasks_api.get_tasks()
        return [Task(board_id=item["board_id"], id=item["id"] ,title=item["title"]) for item in data]