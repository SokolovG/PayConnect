from typing import Any, TypedDict

from src.infrastructure.jm_integration.dto.schemas import JMPayload


class RequestOptions(TypedDict, total=False):
    params: dict[str, str]
    json: dict[str, Any]
    data: JMPayload
    headers: dict[str, str]
