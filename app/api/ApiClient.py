# IMPORTS
import httpx
import json
import logging

# SETUP LOGGER
logger = logging.getLogger(__name__)

# CLASS: API ERROR
class ApiError(Exception):

    # METHOD: INIT
    def __init__(self, message: str, status_code: int | None = None):
        super().__init__(message)

        # SET MESSAGE AND STATUS CODE
        self.message = message
        self.status_code = status_code

# CLASS: API CLIENT
class ApiClient:

    # METHOD: INIT
    def __init__(self, base_url: str, token: str | None = None):

        # DEFINE BASE URL
        self.base_url = base_url.rstrip("/")

        # SET HEADERS
        self.headers = {"Content-Type": "application/json"}

        # ADD TOKEN TO HEADER
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    # METHOD: GET
    async def get(self, path: str):

        # BUILD THE URL PATH
        url = f"{self.base_url}/{path.lstrip('/')}"

        # MAKE API CALL AND RETURN DATA AS JSON
        async with httpx.AsyncClient(headers=self.headers) as client:

            # SEND REQUEST
            response = await client.get(url)

            # HANDLE RESPONSE
            response = self.handle_response(response)

            # RETURN
            return response

    # METHOD: POST
    async def post(self, path: str, data: dict):

        # BUILD THE URL-PATH
        url = f"{self.base_url}/{path.lstrip('/')}"

        # GET JSON STRING
        json_string = json.dumps(data)

        # MAKE API-CALL AND RETURN DATA AS JSON
        async with httpx.AsyncClient(headers=self.headers) as client:

            # SEND REQUEST
            response = await client.post(url, content=json_string)

            # HANDLE RESPONSE
            response = self.handle_response(response)

            # RETURN
            return response

    # METHOD: PATCH
    async def patch(self, path: str, data: dict):

        # BUILD THE URL-PATH
        url = f"{self.base_url}/{path.lstrip('/')}"

        # GET JSON STRING
        json_string = json.dumps(data)

        # MAKE API-CALL AND RETURN DATA AS JSON
        async with httpx.AsyncClient(headers=self.headers) as client:

            # SEND REQUEST
            response = await client.patch(url, content=json_string)

            # HANDLE RESPONSE
            response = self.handle_response(response)

            # RETURN
            return response

    # METHOD: PATCH
    async def delete(self, path: str):

        # BUILD THE URL-PATH
        url = f"{self.base_url}/{path.lstrip('/')}"

        # MAKE API-CALL AND RETURN DATA AS JSON
        async with httpx.AsyncClient(headers=self.headers) as client:

            # SEND REQUEST
            response = await client.delete(url)

            # HANDLE RESPONSE
            response = self.handle_response(response)

            # RETURN
            return response

    # METHOD: HANDLE RESPONSE
    def handle_response(self, response: httpx.Response):

        # CHECK FOR ERROR
        if response.is_error:

            # DEFINE MESSAGE
            message = "REQUEST FAILED"

            # CHECK FOR CONTENT
            if response.content:

                # TRY-CATCH BLOCK
                try:

                    # GET JSON
                    data = response.json()

                # CHECK IF THERE IS ANY DATA
                except ValueError:
                    data = None

                # CHECK FOR ERROR FLAG
                if isinstance(data, dict):
                    message = data.get("message") or data.get("error") or data.get("ERROR") or message

            # RAISE ERROR
            raise ApiError(message, response.status_code)

        # IF RESPONSE HAS CONTENT RETURN IT
        if response.content:
            return response.json()
        else:
            return None