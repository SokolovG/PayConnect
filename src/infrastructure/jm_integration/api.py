import msgspec

from src.infrastructure.jm_integration.client import JMClient
from src.infrastructure.jm_integration.dto.schemas import (
    PaymentCreateRequest,
    PaymentCreateResponse,
    PaymentInfoResponse,
)
from src.infrastructure.jm_integration.enums import HttpMethod


class JMPaymentAPI:
    def __init__(self, client: JMClient) -> None:
        self.client: JMClient = client

    async def get_payment(self, payment_id: str) -> PaymentInfoResponse:
        data = await self.client._make_request(
            method=HttpMethod.GET,
            endpoint=f"/api/v1/payments/{payment_id}",
        )
        return msgspec.convert(data, PaymentInfoResponse)

    async def create_payment(
        self, payment_data: PaymentCreateRequest
    ) -> PaymentCreateResponse:
        data = await self.client._make_request(
            method=HttpMethod.POST,
            endpoint="/api/v1/payments",
            json=msgspec.structs.asdict(payment_data),
        )
        return msgspec.convert(data, PaymentCreateResponse)
