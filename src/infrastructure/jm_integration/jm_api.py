import msgspec

from src.infrastructure.jm_integration.client import JMClient
from src.infrastructure.jm_integration.dto import (
    BalanceResponse,
    OrderResponse,
    PaymentConfirmOrDeclineResponse,
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
        return await self.client._make_request(
            method=HttpMethod.POST,
            endpoint=f"{self.base_url}payments",
            json=msgspec.structs.asdict(payment_data),
            response_model=PaymentCreateResponse,
        )

    async def get_payment(self, payment_token: str) -> PaymentInfoResponse:
        return await self.client._make_request(
            method=HttpMethod.GET,
            endpoint=f"{self.base_url}payments/{payment_token}",
            response_model=PaymentInfoResponse,
        )

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
        return await self.client._make_request(
            method=HttpMethod.GET,
            endpoint=f"{self.base_url}payments",
            params=params,
            response_model=PaymentListResponse,
        )

    async def get_order(self, order_number: int) -> OrderResponse:
        return await self.client._make_request(
            method=HttpMethod.GET,
            endpoint=f"{self.base_url}payments/order/{order_number}",
            response_model=OrderResponse,
        )

    async def get_balance(self, currency: Currency) -> BalanceResponse:
        return await self.client._make_request(
            method=HttpMethod.GET,
            endpoint=f"{self.base_url}balance",
            params={"currency": currency},
            response_model=BalanceResponse,
        )

    async def confirm_payment(self, token: str) -> PaymentConfirmOrDeclineResponse:
        return await self.client._make_request(
            method=HttpMethod.POST,
            endpoint=f"{self.base_url}confirm",
            json={"token": token},
            response_model=PaymentConfirmOrDeclineResponse,
        )

    async def decline_payment(self, token: str) -> PaymentConfirmOrDeclineResponse:
        return await self.client._make_request(
            method=HttpMethod.POST,
            endpoint=f"{self.base_url}decline",
            json={"token": token},
            response_model=PaymentConfirmOrDeclineResponse,
        )
