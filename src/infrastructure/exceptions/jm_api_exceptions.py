from src.infrastructure.exceptions.infrastucture_base_exceptions import (
    InfrastructureBaseError,
)


class JMAPIError(InfrastructureBaseError):
    """Exception raised for errors during interactions with JM API.

    Attributes:
        message (str): Description of the error.
        original_error (Exception): The original mistake that caused this exception.
        status_code (int): HTTP Status Code received from API (if applicable).
    """

    def __init__(
        self, message: str, original_error: Exception = None, status_code: int = None
    ) -> None:
        super().__init__(message)
        self.original_error = original_error
        self.status_code = status_code
