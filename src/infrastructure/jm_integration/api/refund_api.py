import msgspec.structs

from src.infrastructure.jm_integration.api.base_api import BaseAPI
from src.infrastructure.jm_integration.dto.refund import RefundData, RefundResponse
from src.infrastructure.jm_integration.enums import HttpMethod


class JMRefundAPI(BaseAPI):
    """Manage refund operations.

    Provides methods for creating and handling refunds.
    """

    async def create_refund(self, refund_data: RefundData) -> RefundResponse:
        """Create a new refund.

        Args:
            refund_data: Refund creation data

        Returns:
            RefundResponse: Response containing created refund information

        """
        return await self.client._make_request(
            method=HttpMethod.POST,
            endpoint=self.base_url,
            json=msgspec.structs.asdict(refund_data),
            response_model=RefundResponse,
        )
