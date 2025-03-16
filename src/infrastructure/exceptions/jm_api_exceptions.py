from src.infrastructure.exceptions.base_exceptions import APIError


class JMAPIError(APIError):
    """Exception raised specifically for JM API errors."""
