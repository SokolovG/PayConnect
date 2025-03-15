import os

from dotenv import load_dotenv
from httpx import AsyncClient, HTTPError, RequestError

from src.infrastructure.jm_integration.constants import RequestOptions
from src.infrastructure.jm_integration.dto.schemas import JMPayment
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
        self, method: HttpMethod, endpoint: str, **kwargs: RequestOptions
    ) -> JMPayment:
        url = f"{self.base_url}{endpoint}"
        try:
            async with AsyncClient() as client:
                response = await getattr(client, method.value)(
                    url=url, headers=self.headers, **kwargs
                )
                response.raise_for_status()
                response_data = response.json()
                return response_data

        except RequestError as error:
            raise error

        except HTTPError as error:
            raise error
