from app.api.ApiClient import ApiClient

# CLASS FOR TASKS-API
class TasksApi:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    # GET ALL TASKS
    async def get_tasks(self):
        return await self.api_client.get('/tasks')