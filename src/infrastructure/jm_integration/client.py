import logging
from typing import Any, TypeVar

import msgspec
from httpx import AsyncClient, HTTPError, RequestError

from src.infrastructure.exceptions import JMAPIError, MsgspecCustomError
from src.infrastructure.jm_integration.constants import (
    TIMEOUT_FOR_CLIENT,
    RequestOptionsData,
    RequestOptionsJson,
    RequestOptionsParam,
)
from src.infrastructure.jm_integration.enums import HttpMethod
from src.infrastructure.jm_integration.jm_settings import jm_settings

T = TypeVar("T")
logger = logging.getLogger(__name__)


class JMClient:
    def __init__(self) -> None:
        self.api_key: str = jm_settings.JM_TOKEN
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
        logger.info(
            f"Making {method.value.upper()} request to {endpoint}",
            extra={
                "params": str(params),
                "has_json_body": json is not None,
                "has_data": data is not None,
            },
        )
        try:
            async with AsyncClient() as client:
                response = await getattr(client, method.value)(
                    **request_kwargs, timeout=TIMEOUT_FOR_CLIENT
                )
                response.raise_for_status()
                response_data = response.json()

                logger.info(
                    f"Received response from {endpoint}",
                    extra={"status_code": response.status_code},
                )

                if response_model:
                    try:
                        return msgspec.convert(response_data, response_model)
                    except msgspec.ValidationError as error:
                        logger.error(f"Validation error for {endpoint}: {str(error)} ")
                        raise MsgspecCustomError(
                            f"Validation error {str(error)}", status_code=422
                        ) from error
                    except msgspec.DecodeError as error:
                        logger.error(f"Decode error for {endpoint}: {str(error)} ")
                        raise MsgspecCustomError(
                            f"Invalid data format: {str(error)}", status_code=400
                        ) from error
                return response_data

        except RequestError as error:
            logger.error(
                f"Request error for {endpoint}: {str(error)}",
                extra={"method": method.value},
            )
            raise JMAPIError(
                f"Error connecting to JM API at {endpoint}"
                f"(method: {method.value}): {str(error)}",
                original_error=error,
            ) from error

        except HTTPError as error:
            logger.error(
                f"HTTP error for {endpoint}: {str(error)}",
                extra={
                    "method": method.value,
                },
            )
            raise JMAPIError(
                f"HTTP error when accessing JM API at {endpoint}: {str(error)}"
                f"(method: {method.value}): {str(error)}",
                original_error=error,
            ) from error
