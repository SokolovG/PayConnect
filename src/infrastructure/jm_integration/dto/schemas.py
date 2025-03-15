from litestar.dto import MsgspecDTO
from msgspec import Struct

from src.infrastructure.jm_integration.enums import Currency, OperationType, Status


class CustomerInfo(Struct):
    """Client data to create a payment."""

    email: str
    first_name: str
    last_name: str
    phone: str
    country: str = "KE"
    ip: str | None = None


class PaymentCreatePost(Struct):
    """Request for the creation of payment Kes."""

    product: str
    amount: int
    order_number: str
    redirect_success_url: str
    redirect_fail_url: str
    callback_url: str
    customer: CustomerInfo
    currency: Currency = Currency.KES


class RedirectRequestParams(Struct):
    """Parameters for redirect request."""

    pa_req: str  # Converted from PaReq
    term_url: str  # Converted from TermUrl


class RedirectRequest(Struct):
    """Details for redirect request, for example for 3DS."""

    url: str
    params: RedirectRequestParams
    type: str  # e.g. "post"


class PaymentDetails(Struct):
    """Details of payment in the answer."""

    amount: str
    currency: str
    status: str


class PaymentCreateGet(Struct):
    """Answer to a request for a payment."""

    success: bool
    token: str
    processing_url: str  # Converted from processingUrl for
    payment: PaymentDetails
    errors: list[str] = []
    redirect_request: RedirectRequest = None  # Converted from redirectRequest


class CommissionData(Struct):
    """Data on the payment commission."""

    commission_value: float
    commission_fee: float
    commission_amount: float


class PaymentStatusResponse(Struct):
    """Information about payment when requesting status."""

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


class WalletData(Struct):
    """Information about the wallet in the response to the request."""

    available: int
    hold: int
    currency: Currency


class BalanceResponse(Struct):
    """Response to balance request."""

    success: bool
    wallet: WalletData
    errors: list[dict] = []


# DTO FOR LITESTAR
class CustomerDataDTO(MsgspecDTO[CustomerInfo]):
    pass


class PaymentCreateRequestDTO(MsgspecDTO[PaymentCreatePost]):
    pass


class PaymentCreateResponseDTO(MsgspecDTO[PaymentCreateGet]):
    pass


class PaymentStatusResponseDTO(MsgspecDTO[PaymentStatusResponse]):
    pass


class BalanceResponseDTO(MsgspecDTO[BalanceResponse]):
    pass
