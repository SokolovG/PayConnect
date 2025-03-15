from litestar.dto import MsgspecDTO
from msgspec import Struct, field

from src.infrastructure.jm_integration.dto.commision import CommissionData
from src.infrastructure.jm_integration.enums import Currency, OperationType, Status


class PaymentInfo(Struct):
    """Detailed payment information."""

    id: int
    status: Status
    token: str
    product: str
    callback_url: str
    redirect_success_url: str
    redirect_fail_url: str
    amount: int
    created_at: str
    updated_at: str
    extra_return_param: str
    operation_type: OperationType
    order_number: int
    commission_data: CommissionData | None
    currency: Currency = field(default=Currency.KES)


class PaymentInfoResponse(Struct):
    """Full response for payment info request."""

    success: bool
    status: int
    payment: PaymentInfo
    errors: list[str] = []


# Payment Info DTOs.
class PaymentInfoDTO(MsgspecDTO[PaymentInfo]):
    pass


class PaymentInfoResponseDTO(MsgspecDTO[PaymentInfoResponse]):
    pass
