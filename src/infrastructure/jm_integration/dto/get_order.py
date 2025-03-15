from litestar.dto import MsgspecDTO
from msgspec import Struct, field

from src.infrastructure.jm_integration.dto.get_payment import PaymentInfo


class OrderResponse(Struct):
    """Response to an order information request."""

    success: bool
    result: int | None
    status: int
    total_count: int = field(name="totalCount")
    current_page: int = field(name="curentPage")  # literalError from JM Docs.
    per_page: int = field(name="perPage")
    total_page: int = field(name="totalPage")
    payments: list[PaymentInfo]
    errors: list[str] = []


class OrderResponseDTO(MsgspecDTO[OrderResponse]):
    pass
