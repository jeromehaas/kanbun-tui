from app.api.LanesApi import LanesApi
from app.models.Lane import Lane
from app.models.Board import Board
from app.models.Task import Task

# CLASS: LANES SERVICE
class LanesService:

    # METHOD: INIT
    def __init__(self, lanes_api: LanesApi):

        # SETUP FIELDS
        self.lanes_api = lanes_api

    # METHODS: GET ALL BOARDS
    async def get_all_lanes(self, board: Board) -> list[Lane]:

        # GET ALL LANES
        data = await self.lanes_api.get_all_lanes(board.id)

        # RETURN LANES
        return [Lane(
            id=item["id"],
            name=item["name"],
            position=item["position"],
            tasks=[
                Task(
                    id=task["id"],
                    title=task["title"],
                    description=task["description"],
                )
                for task in item["tasks"]
            ])
            for item in data]
