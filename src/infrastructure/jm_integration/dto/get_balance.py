from litestar.dto import MsgspecDTO
from msgspec import Struct

from src.infrastructure.jm_integration.dto.base import ErrorDetail
from src.infrastructure.jm_integration.enums import Currency


class WalletInfo(Struct):
    """Information about the wallet."""

    available: int | float
    hold: int | float
    currency: Currency


class BalanceResponse(Struct):
    """Response to balance request."""

    success: bool
    wallet: WalletInfo
    errors: list[ErrorDetail] = []


class BalanceResponseDTO(MsgspecDTO[BalanceResponse]):
    pass
