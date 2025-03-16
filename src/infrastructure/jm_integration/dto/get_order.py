from msgspec import Struct, field

from src.infrastructure.jm_integration.dto.base import ErrorDetail
from src.infrastructure.jm_integration.dto.get_payment import PaymentInfo


class OrderResponse(Struct):
    """Response structure for order information request.

    Attributes:
        success (bool): Whether the request was successful.
        result (int | None): Result code of the operation.
        status (int): HTTP status code of the response.
        total_count (int): Total number of payments for this order.
        current_page (int): Current page number in pagination.
        per_page (int): Number of results per page.
        total_page (int): Total number of pages available.
        payments (list[PaymentInfo]): List of payment information objects.
        errors (list[ErrorDetail]): List of errors if any occurred.

    Note:
        The field 'current_page' is spelled as 'curentPage' to match the JM API documentation.

    """

    success: bool
    result: int | None
    status: int
    total_count: int = field(name="totalCount")
    current_page: int = field(name="curentPage")  # literalError from JM Docs.
    per_page: int = field(name="perPage")
    total_page: int = field(name="totalPage")
    payments: list[PaymentInfo]
    errors: list[ErrorDetail] = []
