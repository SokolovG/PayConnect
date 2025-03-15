import msgspec

from src.infrastructure.jm_integration.client import JMClient
from src.infrastructure.jm_integration.dto import (
    BalanceResponse,
    OrderResponse,
    PaymentCreateRequest,
    PaymentCreateResponse,
    PaymentInfoResponse,
    PaymentListResponse,
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

    async def get_list_payment(
        self,
        date_from: str | None = None,
        date_to: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        operation_type: str | None = None,
        order_number: str | None = None,
    ) -> PaymentListResponse:
        params = {}
        if date_from:
            params["dateFrom"] = date_from
        if date_to:
            params["dateTo"] = date_to
        if page:
            params["page"] = page
        if per_page:
            params["perPage"] = per_page
        if operation_type:
            params["operationType"] = operation_type
        if order_number:
            params["orderNumber"] = order_number
        response_data = await self.client._make_request(
            method=HttpMethod.GET, endpoint=f"{self.base_url}payments", params=params
        )
        return msgspec.convert(response_data, PaymentListResponse)

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
