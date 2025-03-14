import msgspec

from src.infrastructure.jm_integration.client import JMClient
from src.infrastructure.jm_integration.dto.schemas import JMPayload, JMPayment
from src.infrastructure.jm_integration.enums import HttpMethod


class JMPaymentAPI:
    def __init__(self, client: JMClient) -> None:
        self.client: JMClient = client

    async def get_payment(self, payment_id: str) -> JMPayment:
        return await self.client._make_request(
            method=HttpMethod.GET,
            endpoint=f"/api/v1/payments/{payment_id}",
        )

    async def create_payment(self, payment_data: JMPayload) -> JMPayment:
        return await self.client._make_request(
            method=HttpMethod.POST,
            endpoint="/api/v1/payments",
            json=msgspec.structs.asdict(payment_data),
        )
