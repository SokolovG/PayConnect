from typing import Any, TypedDict

from src.infrastructure.jm_integration.dto.schemas import Payload


class RequestOptions(TypedDict, total=False):
    params: dict[str, str]
    json: dict[str, Any]
    data: Payload
    headers: dict[str, str]
