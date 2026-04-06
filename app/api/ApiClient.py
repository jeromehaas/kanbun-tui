import httpx

class ApiClient:
    def __init__(self, base_url: str, token: str | None = None):
        self.base_url = base_url.rstrip("/")
        self.headers = {"Content-Type": "application/json"}

        # TOKEN IS USED ADD IT TO HEADER
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    # GET FUNCTION
    async def get(self, path: str):

        # BUILD THE URL-PATH
        url = f"{self.base_url}/{path.lstrip('/')}"

        # MAKE API-CALL AND RETURN DATA AS JSON
        async with httpx.AsyncClient(headers=self.headers) as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()