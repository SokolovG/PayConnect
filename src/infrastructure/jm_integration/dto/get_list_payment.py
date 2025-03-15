from litestar.dto import MsgspecDTO
from msgspec import Struct, field

from src.infrastructure.jm_integration.dto import PaymentInfo


class PaymentListRequest(Struct):
    """Request to a payment list."""

    date_from: str | None = field(name="dateFrom")
    date_to: str | None = field(name="dateTo")
    operation_type: str | None = field(name="operationType")
    order_number: int | None = field(name="orderNumber")
    page: int | None = field(default=1)
    per_page: int | None = field(name="perPage", default=20)


class PaymentListResponse(Struct):
    """Response to a payment list request."""

    success: bool
    status: int
    total_count: int = field(name="totalCount")
    current_page: int = field(name="curentPage")
    per_page: int = field(name="perPage")
    total_page: int = field(name="totalPage")
    payments: list[PaymentInfo]
    errors: list = []


class PaymentListRequestDTO(MsgspecDTO[PaymentListRequest]):
    pass


class PaymentListResponseDTO(MsgspecDTO[PaymentListResponse]):
    pass
