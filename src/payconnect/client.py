import os
from typing import Any

from dotenv import load_dotenv

from .constants import HttpMethod, RequestOptions

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

    def _make_request(
        self, method: HttpMethod, endpoint: str, **kwargs: RequestOptions
    ) -> dict[str, Any]:
        return {"": ""}
