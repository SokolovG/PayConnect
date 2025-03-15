from litestar.dto import MsgspecDTO
from msgspec import Struct, field

from src.infrastructure.jm_integration.dto.base import PaymentDetails, RedirectRequest
from src.infrastructure.jm_integration.dto.customer import CustomerInfo
from src.infrastructure.jm_integration.dto.errors import ErrorDetail
from src.infrastructure.jm_integration.enums import Currency


class PaymentCreateRequest(Struct):
    """Request for the creation of payment."""

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
    """Response to a payment creation request."""

    success: bool
    token: str
    processing_url: str | list[dict[str, str]] = field(name="processingUrl")
    payment: PaymentDetails
    errors: list[ErrorDetail] = []
    redirect_request: RedirectRequest | None = field(default=None, name="redirectRequest")
    selector_url: str | None = field(default=None, name="selectorURL")


class PaymentCreateRequestDTO(MsgspecDTO[PaymentCreateRequest]):
    pass


class PaymentCreateResponseDTO(MsgspecDTO[PaymentCreateResponse]):
    pass
