import msgspec.structs

from src.infrastructure.jm_integration.api.base_api import BaseAPI
from src.infrastructure.jm_integration.dto.refund import RefundData, RefundResponse
from src.infrastructure.jm_integration.enums import HttpMethod


class JMRefundAPI(BaseAPI):
    async def create_refund(self, refund_data: RefundData) -> RefundResponse:
        return await self.client._make_request(
            method=HttpMethod.POST,
            endpoint=f"{self.base_url}refunds",
            json=msgspec.structs.asdict(refund_data),
            response_model=RefundResponse,
        )
