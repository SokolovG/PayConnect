import os
from typing import TypeVar, cast

import msgspec
from dotenv import load_dotenv

from src.interfaces.jm_integration.constants import RequestOptions
from src.interfaces.jm_integration.enums import HttpMethod

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

    def _make_request(
        self,
        method: HttpMethod,
        endpoint: str,
        response_type: type[T],
        **kwargs: RequestOptions,
    ) -> T:
        response_data = {"": ""}
        if response_type:
            converted_data = msgspec.convert(response_data, response_type)
            return cast(T, converted_data)

        return cast(T, response_data)
