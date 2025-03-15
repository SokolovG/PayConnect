import msgspec

from src.infrastructure.jm_integration.client import JMClient
from src.infrastructure.jm_integration.dto import (
    BalanceResponse,
    OrderResponse,
    PaymentCreateRequest,
    PaymentCreateResponse,
    PaymentInfoResponse,
)
from src.infrastructure.jm_integration.enums import Currency, HttpMethod


class JMPaymentAPI:
    def __init__(self, client: JMClient) -> None:
        self.client: JMClient = client
        self.base_url: str = "/api/v1/"

    async def create_payment(self, payment_data: PaymentCreateRequest) -> PaymentCreateResponse:
        response_data = await self.client._make_request(
            method=HttpMethod.POST,
            endpoint=f"{self.base_url}payments",
            json=msgspec.structs.asdict(payment_data),
        )
        return msgspec.convert(response_data, PaymentCreateResponse)

    async def get_payment(self, payment_token: str) -> PaymentInfoResponse:
        response_data = await self.client._make_request(
            method=HttpMethod.GET,
            endpoint=f"{self.base_url}payments/{payment_token}",
        )
        return msgspec.convert(response_data, PaymentInfoResponse)

    async def get_order(self, order_number: int) -> OrderResponse:
        response_data = await self.client._make_request(
            method=HttpMethod.GET, endpoint=f"{self.base_url}payments/order/{order_number}"
        )
        return msgspec.convert(response_data, OrderResponse)

    async def get_balance(self, currency: Currency) -> BalanceResponse:
        response_data = await self.client._make_request(
            method=HttpMethod.GET,
            endpoint=f"{self.base_url}balance",
            params={"currency": currency},
        )
        return msgspec.convert(response_data, BalanceResponse)
