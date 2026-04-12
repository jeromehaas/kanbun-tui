from app.api.ApiClient import ApiClient

# CLASS FOR LANES-API
class LanesApi:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    # GET ALL LANES
    async def get_all_lanes(self, id):
        return await self.api_client.get(f'/boards/{ id }/lanes')