from app.api.ApiClient import ApiClient

# CLASS FOR TASKS-API
class TasksApi:
    def __init__(self, base_url: str , token: str | None = None):
        self.api_client = ApiClient(base_url=base_url)

    # GET ALL TASKS
    def get_tasks(self):
        return self.api_client.get('/tasks')