from typing import Any, Final

from src.infrastructure.jm_integration.dto.base import PaymentCreateRequest

RequestOptionsParam: Final = dict[str, str] | None
RequestOptionsJson: Final = dict[str, Any] | None
RequestOptionsData: Final = PaymentCreateRequest | None
RequestOptionsHeaders: Final = dict[str, str] | None
