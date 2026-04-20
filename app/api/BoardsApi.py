from app.api.ApiClient import ApiClient
from app.models.Board import Board


# CLASS FOR BOARDS-API
class BoardsApi:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    # GET ALL BOARDS
    async def get_all_boards(self):
        return await self.api_client.get('/boards')

    async def delete_board_by_id(self, board_id: int):
        return await self.api_client.delete(f'/boards/{board_id}')

    async def create_board(self, board: Board):
        data = {"name": board.name}
        return await self.api_client.post(f'/boards', data)

    async def edit_board_by_id(self, board: Board):
        board_id = board.id
        data = {"name": board.name}

        return await self.api_client.patch(f'/boards/{board_id}', data)