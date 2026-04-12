from app.api.LanesApi import LanesApi
from app.models.Lane import Lane

# WRITES LANES-DATA TO MODEL
class LanesService:
    def __init__(self, lanes_api: LanesApi):
        self.lanes_api = lanes_api

    # GET ALL BOARDS
    async def get_all_lanes(self, id) -> list[Lane]:
        data = await self.lanes_api.get_all_lanes(id)
        return [Lane(
            id=item["id"],
            name=item["name"],
            position=item["position"])
            for item in data]
