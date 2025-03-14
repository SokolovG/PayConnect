from enum import Enum


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
