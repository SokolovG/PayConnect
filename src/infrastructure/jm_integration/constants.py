from typing import Any, TypedDict

from src.infrastructure.jm_integration.dto.schemas import PaymentCreateRequest


class RequestOptions(TypedDict, total=False):
    params: dict[str, str]
    json: dict[str, Any]
    data: PaymentCreateRequest
    headers: dict[str, str]
