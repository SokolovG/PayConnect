from msgspec import Struct


class ErrorDetail(Struct):
    """Подробности ошибки API."""

    code: str
    kind: str
