from litestar.dto import MsgspecDTO
from msgspec import Struct

from src.infrastructure.jm_integration.dto.errors import ErrorDetail
from src.infrastructure.jm_integration.dto.wallet import WalletInfo


class BalanceResponse(Struct):
    """Response to balance request."""

    success: bool
    wallet: WalletInfo
    errors: list[ErrorDetail] = []


class BalanceResponseDTO(MsgspecDTO[BalanceResponse]):
    pass
