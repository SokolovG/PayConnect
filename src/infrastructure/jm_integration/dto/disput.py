from msgspec import Struct

from src.infrastructure.jm_integration.enums import Currency, Status


class DisputeInfo(Struct):
    id: str
    amount: int
    currency: Currency
    investigation_report: str
    status: Status
    merchant_profile_id: int
    user_profile_id: int
    feed_id: int
    created_at: str
    updated_at: str
    dispute_type: int
    reason_code: str
    comment: str


class DisputeResponse(Struct):
    success: bool
    status: int
    disputes: DisputeInfo
