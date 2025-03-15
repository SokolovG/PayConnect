from litestar.dto import MsgspecDTO
from msgspec import Struct

from src.infrastructure.jm_integration.enums import Currency, OperationType, Status


# General data types.
class CustomerInfo(Struct):
    """Client data to create a payment."""

    email: str
    first_name: str
    last_name: str
    phone: str
    country: str = "KE"
    ip: str | None = None


class CommissionData(Struct):
    """Data on the payment commission."""

    commission_value: float
    commission_fee: float
    commission_amount: float


# Payment Create
class PaymentCreateRequest(Struct):
    """Request for the creation of payment."""

    product: str
    amount: int
    order_number: str
    redirect_success_url: str
    redirect_fail_url: str
    callback_url: str
    customer: CustomerInfo
    currency: Currency = Currency.KES


class PaymentDetails(Struct):
    """Details of payment in the creation payment response."""

    amount: str
    currency: str
    status: str


class RedirectRequestParams(Struct):
    """Parameters for redirect request."""

    pa_req: str  # Converted from PaReq
    term_url: str  # Converted from TermUrl


class RedirectRequest(Struct):
    """Details for redirect request, for example, for 3DS."""

    url: str
    params: RedirectRequestParams
    type: str  # e.g. "post"


class PaymentCreateResponse(Struct):
    """Response to a payment creation request."""

    success: bool
    token: str
    processing_url: str  # Converted from processingUrl
    payment: PaymentDetails
    errors: list[str] = []
    redirect_request: RedirectRequest = None  # Converted from redirectRequest


# Payment Info
class PaymentInfo(Struct):
    """Detailed payment information."""

    id: int
    status: Status
    token: str
    currency: Currency
    product: str
    callback_url: str
    redirect_success_url: str
    redirect_fail_url: str
    amount: int
    created_at: str
    updated_at: str
    extra_return_param: str
    operation_type: OperationType
    order_number: str
    commission_data: CommissionData


class PaymentInfoResponse(Struct):
    """Full response for payment info request."""

    success: bool
    status: int
    payment: PaymentInfo
    errors: list[str] = []


# Получение баланса (Balance)
class WalletInfo(Struct):
    """Information about the wallet."""

    available: int
    hold: int
    currency: Currency


class BalanceResponse(Struct):
    """Response to balance request."""

    success: bool
    wallet: WalletInfo
    errors: list[dict] = []


# Payment Create DTOs
class CustomerInfoDTO(MsgspecDTO[CustomerInfo]):
    pass


class PaymentCreateRequestDTO(MsgspecDTO[PaymentCreateRequest]):
    pass


class PaymentCreateResponseDTO(MsgspecDTO[PaymentCreateResponse]):
    pass


# Payment Info DTOs
class PaymentInfoDTO(MsgspecDTO[PaymentInfo]):
    pass


class PaymentInfoResponseDTO(MsgspecDTO[PaymentInfoResponse]):
    pass


# Balance DTOs
class WalletInfoDTO(MsgspecDTO[WalletInfo]):
    pass


class BalanceResponseDTO(MsgspecDTO[BalanceResponse]):
    pass
