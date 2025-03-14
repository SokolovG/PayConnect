from enum import Enum


class HttpMethod(str, Enum):
    GET = "get"
    POST = "post"
    PUT = "put"
    DELETE = "delete"
    PATCH = "patch"


class Currency(str, Enum):
    KES = "KES"


class Status(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    DECLINED = "declined"


class OperationType(str, Enum):
    PAY = "pay"
    PAYOUT = "payout"
