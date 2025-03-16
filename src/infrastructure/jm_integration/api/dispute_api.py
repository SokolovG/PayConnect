from src.infrastructure.jm_integration.api.base_api import BaseAPI
from src.infrastructure.jm_integration.dto.disput import DisputeResponse
from src.infrastructure.jm_integration.enums import HttpMethod, Status


class JMDisputeAPI(BaseAPI):
    async def get_dispute(
        self,
        status: Status | None = None,
        date: str | None = None,
        requisite: str | None = None,
        device: str | None = None,
    ) -> DisputeResponse:
        params = {}
        if status:
            params["status"] = status
        if date:
            params["date"] = date
        if requisite:
            params["requisite"] = requisite
        if device:
            params["device"] = device
        return await self.client._make_request(
            method=HttpMethod.GET,
            endpoint=f"{self.base_url}disputes",
            response_model=DisputeResponse,
            params={}
        )
