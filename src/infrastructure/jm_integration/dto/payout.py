from msgspec import Struct, field

from src.infrastructure.jm_integration.dto.base import ErrorDetail
from src.infrastructure.jm_integration.enums import Currency, Status


class PayoutCustomerInfo(Struct):
    """Data about customer for payout.

    Attributes:
        email (str): Customer's email address.
        ip (str): Customer's IP address.
        address (str | None): Customer's address.
        name (str | None): Customer's first name.
        surname (str | None): Customer's last name.

    """

    email: str
    ip: str
    address: str | None = None
    name: str | None = None
    surname: str | None = None


class CardData(Struct):
    """Data about customer card.

    Attributes:
        pan (str): Primary Account Number (masked card number).
        expires (str): Card expiration date.

    """

    pan: str
    expires: str


class PayoutData(Struct):
    """Payout data for response.

    Attributes:
        amount (int): Payout amount in minor units.
        currency (Currency): Currency of the payout.
        order_number (str): Unique order identifier.
        card (CardData): Information about the card.
        customer (PayoutCustomerInfo): Information about the customer.

    """

    amount: int
    currency: Currency
    order_number: str = field(name="orderNumber")
    card: CardData
    customer: PayoutCustomerInfo


class PayoutDataResponse(Struct):
    """Payout extra data for response.

    Attributes:
        token (str): Unique token for the payout.
        status (Status): Current status of the payout.
        timestamp (str): Timestamp of the payout.

    """

    token: str
    status: Status
    timestamp: str


class PayoutResponse(Struct):
    """Payout data for get request.

    Attributes:
        success (bool): Whether the request was successful.
        errors (ErrorDetail): Details about any errors that occurred.
        payout (PayoutDataResponse): Information about the payout.

    """

    success: bool
    errors: ErrorDetail
    payout: PayoutDataResponse
