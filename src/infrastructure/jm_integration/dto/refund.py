from typing import Literal

from msgspec import Struct, field

from src.infrastructure.jm_integration.dto.base import ErrorDetail
from src.infrastructure.jm_integration.enums import Currency


class RefundData(Struct):
    """Data structure for refund request.

    Attributes:
        token (str): Unique token identifying the transaction.
        amount (int): Amount to be refunded in minor units.

    """

    token: str
    amount: int


class RefundDataResponse(Struct):
    """Data structure for refund information in response.

    Attributes:
        token (str): Unique token identifying the transaction.
        amount (int): Refunded amount in minor units.
        currency (Currency): Currency of the refund.
        status (Literal["approved", "declined"]): Current status of the refund.

    """

    token: str
    amount: int
    currency: Currency
    status: Literal["approved", "declined"]


class RefundResponse(Struct):
    """Response structure for refund request.

    Attributes:
        success (bool): Whether the request was successful.
        errors (ErrorDetail): Details about any errors that occurred.
        token (str): Unique token identifying the transaction.
        processing_url (str): URL for processing the refund.
        refund (RefundDataResponse): Details about the refund.

    """

    success: bool
    errors: ErrorDetail
    token: str
    processing_url: str = field(name="processingUrl")
    refund: RefundDataResponse
