from app.api.TasksApi import TasksApi
from app.models.Task import Task

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