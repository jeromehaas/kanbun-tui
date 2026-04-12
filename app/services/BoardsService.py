from app.api.BoardsApi import BoardsApi
from app.models.Board import Board

# WRITES BOARDS-DATA TO MODEL
class BoardsService:
    def __init__(self, tasks_api: BoardsApi):
        self.tasks_api = tasks_api

    # GET ALL BOARDS
    async def get_all_boards(self) -> list[Board]:
        data = await self.tasks_api.get_all_boards()
        return [Board(
            id=item["id"],
            name=item["name"],
            lanes=item["lanes"]) 
        for item in data]
        