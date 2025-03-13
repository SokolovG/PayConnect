from enum import Enum
from typing import Any, TypedDict

from src.payconnect.dto.schemas import Payload


class HttpMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class Currency(str, Enum):
    KES = "KES"


class Status(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    DECLINED = "declined"


class OperationType(str, Enum):
    PAY = "pay"
    PAYOUT = "payout"


class RequestOptions(TypedDict, total=False):
    params: dict[str, str]
    json: dict[str, Any]
    data: Payload
    headers: dict[str, str]
