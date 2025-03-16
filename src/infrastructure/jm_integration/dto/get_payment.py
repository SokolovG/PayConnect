from msgspec import Struct, field

from src.infrastructure.jm_integration.dto.base import ErrorDetail
from src.infrastructure.jm_integration.enums import Currency, OperationType, Status


class CommissionData(Struct):
    """Data on the payment commission.

    Attributes:
        commission_value (float): Commission value.
        commission_fee (float): Commission fee.
        commission_amount (float): Total commission amount.

    """

    commission_value: float
    commission_fee: float
    commission_amount: float


class PaymentInfo(Struct):
    """Detailed payment information.

    Attributes:
        id (int): Unique identifier of the payment.
        status (Status): Current status of the payment.
        token (str): Unique token for the payment.
        product (str): Product identifier.
        callback_url (str): URL for payment callbacks.
        redirect_success_url (str): URL to redirect on successful payment.
        redirect_fail_url (str): URL to redirect on failed payment.
        amount (int): Payment amount in minor units.
        created_at (str): Timestamp when the payment was created.
        updated_at (str): Timestamp when the payment was last updated.
        extra_return_param (str): Additional parameter to return with callbacks.
        operation_type (OperationType): Type of the payment operation.
        order_number (int | str): Unique order identifier.
        commission_data (CommissionData | None): Information about commission.
        currency (Currency): Currency of the payment (defaults to KES).

    """

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
    """Full response for payment info request.

    Attributes:
        success (bool): Whether the request was successful.
        status (int): HTTP status code of the response.
        payment (PaymentInfo): Detailed payment information.
        errors (list[ErrorDetail]): List of errors if any occurred.

    """

    success: bool
    status: int
    payment: PaymentInfo
    errors: list[ErrorDetail] = []
