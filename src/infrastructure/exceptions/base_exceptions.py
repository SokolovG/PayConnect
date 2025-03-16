class InfrastructureBaseError(Exception):
    """Base class for all exceptions in the infrastructure layer."""


class APIError(InfrastructureBaseError):
    def __init__(
        self, message: str, original_error: Exception = None, status_code: int = None
    ) -> None:
        super().__init__(message)
        self.original_error = original_error
        self.status_code = status_code
