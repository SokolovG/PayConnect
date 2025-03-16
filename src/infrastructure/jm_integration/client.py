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
    """Client for making API requests to JM payment service.

    This class provides methods to interact with the JM API for payment processing.

    Attributes:
        api_key: Authentication token for JM API
        base_url: Base URL for all API requests
        headers: HTTP headers used for all requests including authorization

    """

    def __init__(self) -> None:
        """Initialize JM client with API key and base URL.

        Instance Attributes:
            api_key: Authentication token retrieved from settings
            base_url: Base URL for JM API endpoints
            headers: Default HTTP headers including authorization and content type

        """
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
        """Make HTTP request to JM API.

        Args:
            method: HTTP method to use (GET, POST, etc.)
            endpoint: API endpoint path to call
            response_model: Optional type for response data validation and conversion
            params: Optional URL parameters
            json: Optional JSON data for request body
            data: Optional form data for request body

        Returns:
            Parsed response data, either as specified response_model or raw dictionary

        Raises:
            JMAPIError: When connection or HTTP errors occur
            MsgspecCustomError: When response validation fails

        """
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
                            f"Validation error {str(error)}",
                            status_code=422,
                            original_error=error,
                        ) from error
                    except msgspec.DecodeError as error:
                        logger.error(f"Decode error for {endpoint}: {str(error)} ")
                        raise MsgspecCustomError(
                            f"Invalid data format: {str(error)}",
                            status_code=400,
                            original_error=error,
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
