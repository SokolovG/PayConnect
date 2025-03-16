import os
from typing import Any, TypeVar

import msgspec
from dotenv import load_dotenv
from httpx import AsyncClient, HTTPError, RequestError

from src.infrastructure.exceptions import JMAPIError, MsgspecCustomError
from src.infrastructure.jm_integration.constants import (
    TIMEOUT_FOR_CLIENT,
    RequestOptionsData,
    RequestOptionsJson,
    RequestOptionsParam,
)
from src.infrastructure.jm_integration.enums import HttpMethod

load_dotenv()
API_KEY = os.getenv("JM_TOKEN")


T = TypeVar("T")


class JMClient:
    def __init__(self) -> None:
        self.api_key: str = API_KEY
        self.base_url: str = "https://business.processinprocess.com"
        self.headers: dict[str, str] = {
            "authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        self.client = AsyncClient()

    async def _make_request(
        self,
        method: HttpMethod,
        endpoint: str,
        *,
        response_model: type[T] = None,
        params: RequestOptionsParam = None,
        json: RequestOptionsJson = None,
        data: RequestOptionsData = None,
    ) -> T | dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        request_kwargs = {"url": url, "headers": self.headers}
        if params is not None:
            request_kwargs["params"] = params
        if json is not None:
            request_kwargs["json"] = json
        if data is not None:
            request_kwargs["data"] = data

        try:
            async with AsyncClient() as client:
                response = await getattr(client, method.value)(
                    **request_kwargs, timeout=TIMEOUT_FOR_CLIENT
                )
                response.raise_for_status()
                response_data = response.json()

                if response_model:
                    try:
                        return msgspec.convert(response_data, response_model)
                    except msgspec.ValidationError as error:
                        raise MsgspecCustomError(
                            f"Validation error {str(error)}", status_code=422
                        ) from error
                    except msgspec.DecodeError as error:
                        raise MsgspecCustomError(
                            f"Invalid data format: {str(error)}", status_code=400
                        ) from error
                return response_data

        except RequestError as error:
            raise JMAPIError(
                f"Error connecting to JM API at {endpoint}"
                f"(method: {method.value}): {str(error)}",
                original_error=error,
            ) from error

        except HTTPError as error:
            raise JMAPIError(
                f"HTTP error when accessing JM API at {endpoint}: {str(error)}"
                f"(method: {method.value}): {str(error)}",
                original_error=error,
            ) from error
