import msgspec.structs

from src.infrastructure.jm_integration.api.base_api import BaseAPI
from src.infrastructure.jm_integration.dto.payout import PayoutData, PayoutResponse
from src.infrastructure.jm_integration.enums import HttpMethod


class JMPayoutAPI(BaseAPI):
    """Manage payout operations.

    Provides methods for creating and handling payouts.
    """

    async def create_payout(self, payout_data: PayoutData) -> PayoutResponse:
        """Create a new payout.

        Args:
            payout_data: Payout creation data

        Returns:
            PayoutResponse: Response containing created payout information

        """
        return await self.client._make_request(
            method=HttpMethod.POST,
            endpoint=self.payout_url,
            json=msgspec.structs.asdict(payout_data),
            response_model=PayoutResponse,
        )
