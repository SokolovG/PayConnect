from litestar.dto import MsgspecDTO
from msgspec import Struct

from src.infrastructure.jm_integration.enums import Currency, OperationType, Status


class JMPayment(Struct):
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


class JMPaymentDTO(MsgspecDTO[JMPayment]):
    pass


class JMWallet(Struct):
    available: int
    hold: int
    currency: Currency


class JMWalletDTO(MsgspecDTO[JMWallet]):
    pass


class JMBalance(Struct):
    success: bool
    errors: list[str]
    wallet: JMWallet


class JMBalanceDTO(MsgspecDTO[JMBalance]):
    pass


class JMCustomer(Struct):
    email: str
    first_name: str
    last_name: str
    ip: str
    phone: str
    country: str


class JMCustomerDTO(MsgspecDTO[JMCustomer]):
    pass


class JMPayload(Struct):
    product: str
    amount: int
    currency: Currency
    order_number: str
    redirect_success_url: str
    redirect_fail_url: str
    callback_url: str
    customer: JMCustomer


class PayloadDTO(MsgspecDTO[JMPayload]):
    pass
