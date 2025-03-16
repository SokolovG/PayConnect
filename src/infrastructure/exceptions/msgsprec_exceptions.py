from src.infrastructure.exceptions.base_exceptions import APIError


class MsgspecCustomError(APIError):
    """Exception raised specifically for msgspec validation or decode/encode errors."""
