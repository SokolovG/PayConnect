import msgspec

from src.infrastructure.jm_integration.api.base_api import BaseAPI
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


class JMPaymentAPI(BaseAPI):
    """Manage payment operations.

    Provides methods for creating, retrieving, and managing payments.
    """

    async def create_payment(self, payment_data: PaymentCreateRequest) -> PaymentCreateResponse:
        """Create a new payment.

        Args:
            payment_data: Payment creation data

        Returns:
            PaymentCreateResponse: Response containing created payment information

        """
        return await self.client._make_request(
            method=HttpMethod.POST,
            endpoint=self.payment_url,
            json=msgspec.structs.asdict(payment_data),
            response_model=PaymentCreateResponse,
        )

    async def get_payment(self, payment_token: str) -> PaymentInfoResponse:
        """Retrieve payment information by token.

        Args:
            payment_token: Unique payment identifier token

        Returns:
            PaymentInfoResponse: Response containing payment details

        """
        return await self.client._make_request(
            method=HttpMethod.GET,
            endpoint=f"{self.payment_url}{payment_token}",
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
        """Retrieve a filtered list of payments.

        Args:
            date_from: Start date for filtering payments
            date_to: End date for filtering payments
            page: Page number for pagination
            per_page: Number of items per page
            operation_type: Type of payment operation
            order_number: Order identifier for filtering

        Returns:
            PaymentListResponse: Response containing list of payments

        """
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
            endpoint=self.payment_url,
            params=params,
            response_model=PaymentListResponse,
        )

    async def get_order(self, order_number: int) -> OrderResponse:
        """Retrieve order information by order number.

        Args:
            order_number: Unique order identifier

        Returns:
            OrderResponse: Response containing order details

        """
        return await self.client._make_request(
            method=HttpMethod.GET,
            endpoint=f"{self.payment_url}/order/{order_number}",
            response_model=OrderResponse,
        )

    async def get_balance(self, currency: Currency) -> BalanceResponse:
        """Retrieve balance information for a specific currency.

        Args:
            currency: Currency enum value

        Returns:
            BalanceResponse: Response containing balance information

        """
        return await self.client._make_request(
            method=HttpMethod.GET,
            endpoint=f"{self.base_url}balance",
            params={"currency": currency},
            response_model=BalanceResponse,
        )

    async def confirm_payment(self, token: str) -> PaymentConfirmOrDeclineResponse:
        """Confirm a pending payment.

        Args:
            token: Payment token to confirm

        Returns:
            PaymentConfirmOrDeclineResponse: Response containing a confirmation result

        """
        return await self.client._make_request(
            method=HttpMethod.POST,
            endpoint=f"{self.payment_url}/confirm",
            json={"token": token},
            response_model=PaymentConfirmOrDeclineResponse,
        )

    async def decline_payment(self, token: str) -> PaymentConfirmOrDeclineResponse:
        """Decline a pending payment.

        Args:
            token: Payment token to decline

        Returns:
            PaymentConfirmOrDeclineResponse: Response containing decline result

        """
        return await self.client._make_request(
            method=HttpMethod.POST,
            endpoint=f"{self.payment_url}/decline",
            json={"token": token},
            response_model=PaymentConfirmOrDeclineResponse,
        )
