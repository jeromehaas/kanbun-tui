from app.api.ApiClient import ApiClient
from app.models.Task import Task
from app.models.Lane import Lane
from app.models.Board import Board

# CLASS FOR TASKS-API
class TasksApi:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    # GET ALL TASKS
    async def get_tasks(self):
        return await self.api_client.get('/tasks')

    # CREATE TASK
    async def create_task(self, board:Board, lane:Lane, task:Task ):
        return await self.api_client.post(f'/boards/{board.id}/lanes/{lane.id}/tasks',
                                          {"title": task.title,
                                                "description": task.description,
                                              })

    # EDIT TASK
    async def edit_task(self,board:Board, lane:Lane, task:Task):
        return await self.api_client.patch(f'/boards/{board.id}/lanes/{lane.id}/tasks/{task.id}',
                                          {"title": task.title,
                                           "description": task.description,
                                           })

    # DELETE TASK
    async def delete_task(self,board:Board, lane:Lane, task:Task):
        return await self.api_client.delete(f'/boards/{board.id}/lanes/{lane.id}/tasks/{task.id}')
