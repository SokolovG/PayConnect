from msgspec import Struct, field


class PaymentConfirmRequest(Struct):
    """Request to confirm a two-step payment."""

    token: str


class PaymentDeclineRequest(Struct):
    """Request to decline a two-step payment."""

    token: str


class PaymentConfirmDetails(Struct):
    """Details of a confirmed/declined payment."""

    amount: int
    gateway_amount: int = field(name="gateway_amount")
    currency: str
    status: str
    two_stage_mode: bool = field(name="two_stage_mode")


class PaymentConfirmResponse(Struct):
    """Response to a payment confirmation or decline request."""

    success: bool
    result: int
    status: int
    payment: PaymentConfirmDetails
