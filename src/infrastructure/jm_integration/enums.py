from enum import Enum


class HttpMethod(str, Enum):
    GET = "get"
    POST = "post"


class Currency(str, Enum):
    KES = "KES"
    EUR = "EUR"
    USD = "USD"
    GHS = "GHS"
    UGX = "UGX"
    NGN = "NGN"
    RUB = "RUB"


class Status(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    DECLINED = "declined"
    INIT = "init"
    SENT = "sent"
    EXPIRED = "expired"
    PROCESSING = "processing"


class OperationType(str, Enum):
    PAY = "pay"
    PAYOUT = "payout"
