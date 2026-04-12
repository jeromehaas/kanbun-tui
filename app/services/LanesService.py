from app.api.LanesApi import LanesApi
from app.models.Lane import Lane

# CLASS: LANES SERVICE
class LanesService:

    # METHOD: INIT
    def __init__(self, lanes_api: LanesApi):

        # SETUP FIELDS
        self.lanes_api = lanes_api

    # METHODS: GET ALL BOARDS
    async def get_all_lanes(self, id) -> list[Lane]:

        # GET ALL LANES
        data = await self.lanes_api.get_all_lanes(id)

        # RETURN LANES
        return [Lane(
            id=item["id"],
            name=item["name"],
            position=item["position"],
            tasks=item["tasks"])
            for item in data]
