# IMPORTS
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

    # METHOD: GET ALL BOARDS
    async def get_all_lanes(self, board: Board) -> list[Lane]:

        # GET ALL LANES
        data = await self.lanes_api.get_all_lanes(board)

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
                    position=task["position"],
                )
                for task in item["tasks"]
            ])
            for item in data]

    # METHOD: CREATE LANE
    async def create_lane(self, board: Board, data: Lane) -> Lane:

        # GET ALL LANES
        data = await self.lanes_api.create_lane(board, data)

        # RETURN LANE
        return Lane(
            id=data["id"],
            name=data["name"],
            position=data["position"],
            tasks=[]
        )

    # METHOD: DELETE LANE
    async def delete_lane(self, board: Board, lane: Lane) -> Lane:

        # GET ALL LANES
        data = await self.lanes_api.delete_lane(board, lane)

        # RETURN LANE
        return Lane(
            id=data["id"],
            name=data["name"],
            position=data["position"],
            tasks=[]
        )

    # METHOD: EDIT LANE
    async def edit_lane(self, board: Board, lane: Lane, data: Lane) -> Lane:

        # GET ALL LANES
        data = await self.lanes_api.edit_lane(board, lane, data)

        # RETURN LANES
        return Lane(
            id=data["id"],
            name=data["name"],
            position=data["position"],
            tasks=[
                Task(
                    id=task["id"],
                    title=task["title"],
                    description=task["description"],
                    position=task["position"],
                )
                for task in data.get("tasks", [])
            ])

    # METHOD: MOVE LANE
    async def move_lane(self, board: Board, lane: Lane, direction: str) -> Lane:

        # MOVE LANE
        data = await self.lanes_api.move_lane(board, lane, direction)

        # RETURN LANE
        return Lane(
            id=data["id"],
            name=data["name"],
            position=data["position"],
            tasks=[
                Task(
                    id=task["id"],
                    title=task["title"],
                    description=task["description"],
                    position=task["position"],
                )
                for task in data.get("tasks", [])
            ])

