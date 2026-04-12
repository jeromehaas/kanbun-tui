from app.api.BoardsApi import BoardsApi
from app.models.Board import Board

# CLASS: BOARDS SERVICE
class BoardsService:

    # METHOD: INIT
    def __init__(self, tasks_api: BoardsApi):

        # SETUP FIELDS
        self.tasks_api = tasks_api

    # METHOD: GET ALL BOARDS
    async def get_all_boards(self) -> list[Board]:

        # GET ALL BOARDS
        data = await self.tasks_api.get_all_boards()

        # RETURN BOARD
        return [Board(
            id=item["id"],
            name=item["name"],
            lanes=item["lanes"]) 
            for item in data]
        