from app.api.ApiClient import ApiClient

# CLASS FOR BOARDS-API
class BoardsApi:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    # GET ALL BOARDS
    async def get_all_boards(self):
        return await self.api_client.get('/boards')

    async def delete_board_by_id(self, board_id: int):
        return await self.api_client.delete(f'/boards/{board_id}')

