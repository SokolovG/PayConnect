from msgspec import Struct

from src.infrastructure.jm_integration.enums import Currency


class WalletInfo(Struct):
    """Information about the wallet."""

    available: int | float
    hold: int | float
    currency: Currency
