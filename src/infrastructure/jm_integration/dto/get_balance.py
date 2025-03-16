from msgspec import Struct

from src.infrastructure.jm_integration.dto.base import ErrorDetail
from src.infrastructure.jm_integration.enums import Currency


class WalletInfo(Struct):
    """Information about a user's wallet.

    Attributes:
        available (int | float): Available balance in the wallet.
        hold (int | float): Amount on hold/frozen in the wallet.
        currency (Currency): Currency of the wallet.

    """

    available: int | float
    hold: int | float
    currency: Currency


class BalanceResponse(Struct):
    """Response structure for balance inquiry.

    Attributes:
        success (bool): Whether the request was successful.
        wallet (WalletInfo): Information about the wallet.
        errors (list[ErrorDetail]): List of errors if any occurred.

    """

    success: bool
    wallet: WalletInfo
    errors: list[ErrorDetail] = []
