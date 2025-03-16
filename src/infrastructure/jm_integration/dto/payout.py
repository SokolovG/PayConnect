from msgspec import Struct, field

from src.infrastructure.jm_integration.dto.base import ErrorDetail
from src.infrastructure.jm_integration.enums import Currency, Status


class PayoutCustomerInfo(Struct):
    email: str
    ip: str
    address: str | None = None
    name: str | None = None
    surname: str | None = None


class CardData(Struct):
    pan: str
    expires: str


class PayoutData(Struct):
    amount: int
    currency: Currency
    order_number: str = field(name="orderNumber")
    card: CardData
    customer: PayoutCustomerInfo


class PayoutDataResponse(Struct):
    token: str
    status: Status
    timestamp: str


class PayoutResponse(Struct):
    success: bool
    errors: ErrorDetail
    payout: PayoutDataResponse
