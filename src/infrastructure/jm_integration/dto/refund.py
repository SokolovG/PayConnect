from typing import Literal

from msgspec import Struct, field

from src.infrastructure.jm_integration.dto.base import ErrorDetail
from src.infrastructure.jm_integration.enums import Currency


class RefundData(Struct):
    token: str
    amount: int


class RefundDataResponse(Struct):
    token: str
    amount: int
    currency: Currency
    status: Literal["approved", "declined"]


class RefundResponse(Struct):
    success: bool
    errors: ErrorDetail
    token: str
    processing_url: str = field(name="processingUrl")
    refund: RefundDataResponse
