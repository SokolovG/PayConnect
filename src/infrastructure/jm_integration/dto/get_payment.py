from litestar.dto import MsgspecDTO
from msgspec import Struct, field

from src.infrastructure.jm_integration.dto.commision import CommissionData
from src.infrastructure.jm_integration.dto.errors import ErrorDetail
from src.infrastructure.jm_integration.enums import Currency, OperationType, Status


class PaymentInfo(Struct):
    """Detailed payment information."""

    id: int
    status: Status
    token: str
    product: str
    callback_url: str
    redirect_success_url: str = field(name="redirectSuccessUrl")
    redirect_fail_url: str = field(name="redirectFailUrl")
    amount: int
    created_at: str
    updated_at: str
    extra_return_param: str = field(name="extraReturnParam")
    operation_type: OperationType
    order_number: int | str
    commission_data: CommissionData | None
    currency: Currency = field(default=Currency.KES)


class PaymentInfoResponse(Struct):
    """Full response for payment info request."""

    success: bool
    status: int
    payment: PaymentInfo
    errors: list[ErrorDetail] = []


# Payment Info DTOs.
class PaymentInfoDTO(MsgspecDTO[PaymentInfo]):
    pass


class PaymentInfoResponseDTO(MsgspecDTO[PaymentInfoResponse]):
    pass
