from msgspec import Struct

from src.infrastructure.jm_integration.enums import Currency, Status


class DisputeInfo(Struct):
    """Info about dispute.

    Attributes:
        id (str): Unique identifier of the dispute.
        amount (int): Disputed amount in minor units.
        currency (Currency): Currency of the disputed amount.
        investigation_report (str): Report of the investigation.
        status (Status): Current status of the dispute.
        merchant_profile_id (int): ID of the merchant profile.
        user_profile_id (int): ID of the user profile.
        feed_id (int): ID of the feed.
        created_at (str): Timestamp when the dispute was created.
        updated_at (str): Timestamp when the dispute was last updated.
        dispute_type (int): Type of the dispute.
        reason_code (str): Code indicating the reason for the dispute.
        comment (str): Additional comment on the dispute.

    """

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
    """Response to a dispute get request.

    Attributes:
        success (bool): Whether the request was successful.
        status (int): HTTP status code of the response.
        disputes (DisputeInfo): Information about the dispute.

    """

    success: bool
    status: int
    disputes: DisputeInfo
