from msgspec import Struct, field

from src.infrastructure.jm_integration.dto import PaymentInfo
from src.infrastructure.jm_integration.dto.base import ErrorDetail


class PaymentListRequest(Struct):
    """Request structure for retrieving a list of payments.

    Attributes:
        date_from (str | None): Start date for filtering payments (ISO format).
        date_to (str | None): End date for filtering payments (ISO format).
        operation_type (str | None): Type of operation to filter by.
        order_number (int | None): Specific order number to filter by.
        page (int | None): Page number for pagination (defaults to 1).
        per_page (int | None): Number of results per page (defaults to 20).

    """

    date_from: str | None = field(name="dateFrom")
    date_to: str | None = field(name="dateTo")
    operation_type: str | None = field(name="operationType")
    order_number: int | None = field(name="orderNumber")
    page: int | None = field(default=1)
    per_page: int | None = field(name="perPage", default=20)


class PaymentListResponse(Struct):
    """Response structure for payment list request.

    Attributes:
        success (bool): Whether the request was successful.
        status (int): HTTP status code of the response.
        total_count (int): Total number of payments matching the filter.
        current_page (int): Current page number in pagination.
        per_page (int): Number of results per page.
        total_page (int): Total number of pages available.
        payments (list[PaymentInfo]): List of payment information objects.
        errors (list[ErrorDetail]): List of errors if any occurred.

    """

    success: bool
    status: int
    total_count: int = field(name="totalCount")
    current_page: int = field(name="curentPage")
    per_page: int = field(name="perPage")
    total_page: int = field(name="totalPage")
    payments: list[PaymentInfo]
    errors: list[ErrorDetail] = []
