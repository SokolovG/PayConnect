import os
from typing import Any

from dotenv import load_dotenv
from httpx import AsyncClient, HTTPError, RequestError

from src.infrastructure.exceptions.jm_api_exceptions import JMAPIError
from src.infrastructure.jm_integration.constants import (
    RequestOptionsData,
    RequestOptionsHeaders,
    RequestOptionsJson,
    RequestOptionsParam,
)
from src.infrastructure.jm_integration.enums import HttpMethod

load_dotenv()
API_KEY = os.getenv("JM_TOKEN")


class JMClient:
    def __init__(self) -> None:
        self.api_key: str = API_KEY
        self.base_url: str = "https://business.processinprocess.com"
        self.headers: dict[str, str] = {
            "authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    async def _make_request(
        self,
        method: HttpMethod,
        endpoint: str,
        *,
        params: RequestOptionsParam = None,
        json: RequestOptionsJson = None,
        data: RequestOptionsData = None,
        headers: RequestOptionsHeaders = None,
    ) -> dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        request_kwargs = {"url": url, "headers": self.headers}
        if params is not None:
            request_kwargs["params"] = params
        if json is not None:
            request_kwargs["json"] = json
        if data is not None:
            request_kwargs["data"] = data
        if headers is not None:
            # Combine the transferred headlines with default.
            request_kwargs["headers"] = {**self.headers, **headers}

        try:
            async with AsyncClient() as client:
                response = await getattr(client, method.value)(**request_kwargs)
                response.raise_for_status()
                response_data = response.json()
                return response_data

        except RequestError as error:
            raise JMAPIError(
                f"Error connecting to JM API at {endpoint}: {str(error)}",
                original_error=error,
            ) from error

        except HTTPError as error:
            raise JMAPIError(
                f"HTTP error when accessing JM API at {endpoint}: {str(error)}",
                original_error=error,
            ) from error
