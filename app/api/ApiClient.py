import httpx

class ApiClient:
    def __init__(self, base_url: str, token: str | None = None):
        self.base_url = base_url.rstrip("/")
        self.headers = {"Content-Type": "application/json"}

        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    async def get(self, path: str):
        url = f"{self.base_url}/{path.lstrip('/')}"
        async with httpx.AsyncClient(headers=self.headers) as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()