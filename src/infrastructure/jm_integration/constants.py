from typing import Any, Final

from src.infrastructure.jm_integration.dto import PaymentCreateRequest

RequestOptionsParam: Final = dict[str, str] | None
RequestOptionsJson: Final = dict[str, Any] | None
RequestOptionsData: Final = PaymentCreateRequest | None

TIMEOUT_FOR_CLIENT: Final[float] = 30.0
