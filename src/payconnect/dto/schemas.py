from litestar.dto import MsgspecDTO
from msgspec import Struct

from src.payconnect.constants import Currency, OperationType, Status


class Payment(Struct):
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
    order_number: str
    commission_data: dict[str, float]
    currency: Currency


class PaymentDTO(MsgspecDTO[Payment]):
    pass


class Wallet(Struct):
    available: int
    hold: int
    currency: Currency


class WalletDTO(MsgspecDTO[Wallet]):
    pass


class Balance(Struct):
    success: bool
    errors: list[str]
    wallet: Wallet


class BalanceDTO(MsgspecDTO[Balance]):
    pass


class Customer(Struct):
    email: str
    first_name: str
    last_name: str
    ip: str
    phone: str
    country: str


class CustomerDTO(MsgspecDTO[Customer]):
    pass


class Payload(Struct):
    product: str
    amount: int
    currency: Currency
    order_number: str
    redirect_success_url: str
    redirect_fail_url: str
    callback_url: str
    customer: Customer


class PayloadDTO(MsgspecDTO[Payload]):
    pass
