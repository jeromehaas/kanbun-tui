# IMPORTS
from app.api.ApiClient import ApiClient
from app.models.Lane import Lane
from app.models.Board import Board

# CLASS: LANES API
class LanesApi:

    # METHOD: INIT
    def __init__(self, api_client: ApiClient):

        # SETUP API CLIENT
        self.api_client = api_client

    # FUNCTION: GET ALL LANES
    async def get_all_lanes(self, board: Board):

        # SEND REQUEST
        return await self.api_client.get(
            f'/boards/{board.id}/lanes'
        )

    # FUNCTION: GET ALL LANES
    async def create_lane(self, board: Board, data: Lane):

        # SEND REQUEST
        return await self.api_client.post(
            f'/boards/{board.id}/lanes',
            {
                "name": data.name,
            }
        )

    # FUNCTION: DELETE LANE
    async def delete_lane(self, board: Board, lane: Lane):

        # SEND REQUEST
        return await self.api_client.delete(
            f'/boards/{board.id}/lanes/{lane.id}'
        )

    # FUNCTION: EDIT LANE
    async def edit_lane(self, board: Board, lane: Lane, data: Lane):

        # SEND REQUEST
        return await self.api_client.patch(
            f'/boards/{board.id}/lanes/{lane.id}',
            {
               "name": data.name,
            }
        )

    # FUNCTION: MOVE LANE
    async def move_lane(self, board: Board, lane: Lane, direction: str):

        # GET CURRENT POSITION
        current_position = lane.position

        # GET UPDATED POSITION
        if direction == "left":
            updated_position = max(1, current_position - 1)
        else:
            updated_position = current_position + 1

        return await self.api_client.patch(
            f'/boards/{board.id}/lanes/{lane.id}',
            {
               "position": updated_position,
            }
        )