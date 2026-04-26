# IMPORTS
from app.api.ApiClient import ApiClient
from app.models.Board import Board

# CLASS: BOARDS API
class BoardsApi:

    # METHOD: INIT
    def __init__(self, api_client: ApiClient):

        # SETUP API CLIENT
        self.api_client = api_client

    # METHOD: GET ALL BOARDS
    async def get_all_boards(self):

        # SEND REQUEST
        return await self.api_client.get('/boards')

    # METHOD: DELETE BOARD BY ID
    async def delete_board_by_id(self, board_id: int):

        # SEND REQUEST
        return await self.api_client.delete(
            f'/boards/{board_id}'
        )

    # METHOD: CREATE NEW BOARD
    async def create_board(self, board: Board):

        # GET DATA
        data = {
            "name": board.name
        }

        # SEND REQUEST
        return await self.api_client.post(
            f'/boards', data
        )

    # METHOD: EDIT BOARD BY ID
    async def edit_board_by_id(self, board: Board):

        # GET BOARD ID
        board_id = board.id

        # SEND REQUEST
        return await self.api_client.patch(
            f'/boards/{board_id}',
            {
                "name": board.name
            }
        )
