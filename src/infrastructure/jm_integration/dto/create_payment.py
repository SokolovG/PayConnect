from msgspec import Struct, field

from src.infrastructure.jm_integration.dto import CustomerInfo
from src.infrastructure.jm_integration.dto.base import (
    ErrorDetail,
    PaymentDetails,
    RedirectRequest,
)
from src.infrastructure.jm_integration.enums import Currency


class PaymentCreateRequest(Struct):
    """Request for the creation of payment.

    Attributes:
        product (str): Product identifier.
        amount (int): Payment amount in minor units.
        callback_url (str): URL for payment callbacks.
        customer (CustomerInfo): Information about the customer.
        locale (str | None): Locale for the payment interface.
        recurring (bool | None): Whether this is a recurring payment.
        order_number (str | None): Unique order identifier.
        redirect_success_url (str | None): URL to redirect on successful payment.
        redirect_fail_url (str | None): URL to redirect on failed payment.
        extra_return_param (str | None): Additional parameter to return with callbacks.
        wallet_token (str | None): Token for wallet operations.
        recurring_token (str | None): Token for recurring payments.
        need_confirmation (bool | None): Whether payment needs confirmation.
        currency (Currency): Currency of the payment (defaults to KES).

    """

    # Mandatory fields
    product: str
    amount: int
    callback_url: str = field(name="callbackUrl")
    customer: CustomerInfo

    # Optional fields with camelCase mapping
    locale: str | None
    recurring: bool | None
    order_number: str | None = field(default=None, name="orderNumber")
    redirect_success_url: str | None = field(default=None, name="redirectSuccessUrl")
    redirect_fail_url: str | None = field(default=None, name="redirectFailUrl")
    extra_return_param: str | None = field(default=None, name="extraReturnParam")
    wallet_token: str | None = field(default=None, name="walletToken")
    recurring_token: str | None = field(default=None, name="recurringToken")
    need_confirmation: bool | None = field(default=None, name="needConfirmation")
    currency: Currency = field(default=Currency.KES, name="currency")


class PaymentCreateResponse(Struct):
    """Response to a payment creation request.

    Attributes:
        success (bool): Whether the request was successful.
        token (str): Unique token for the payment.
        processing_url (str | list[dict[str, str]]): URL for processing the payment.
        payment (PaymentDetails): Details of the created payment.
        errors (list[ErrorDetail]): List of errors if any occurred.
        redirect_request (RedirectRequest | None): Redirect information if needed.
        selector_url (str | None): URL for payment method selection.

    """

    success: bool
    token: str
    processing_url: str | list[dict[str, str]] = field(name="processingUrl")
    payment: PaymentDetails
    errors: list[ErrorDetail] = []
    redirect_request: RedirectRequest | None = field(default=None, name="redirectRequest")
    selector_url: str | None = field(default=None, name="selectorURL")
