from src.infrastructure.jm_integration.api.base_api import BaseAPI
from src.infrastructure.jm_integration.dto.payout import PayoutData, PayoutResponse
from src.infrastructure.jm_integration.enums import HttpMethod


class JMPayoutAPI(BaseAPI):
    async def create_payout(self, payout_data: PayoutData) -> PayoutResponse:
        return await self.client._make_request(
            method=HttpMethod.POST,
            endpoint=f"{self.base_url}payouts",
            json="",
            response_model=PayoutResponse,
        )
