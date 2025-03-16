from msgspec import Struct


class PaymentConfirmDetails(Struct):
    """Details of a confirmed/declined payment."""

    amount: int
    gateway_amount: int
    currency: str
    status: str
    two_stage_mode: bool


class PaymentConfirmOrDeclineResponse(Struct):
    """Response to a payment confirmation or decline request."""

    success: bool
    result: int
    status: int
    payment: PaymentConfirmDetails
