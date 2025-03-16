from msgspec import Struct


class PaymentConfirmDetails(Struct):
    """Details of a confirmed/declined payment.

    Attributes:
        amount (int): Amount of the payment in minor units.
        gateway_amount (int): Amount processed by the gateway in minor units.
        currency (str): Currency code of the payment.
        status (str): Current status of the payment.
        two_stage_mode (bool): Whether two-stage payment mode is enabled.

    """

    amount: int
    gateway_amount: int
    currency: str
    status: str
    two_stage_mode: bool


class PaymentConfirmOrDeclineResponse(Struct):
    """Response to a payment confirmation or decline request.

    Attributes:
        success (bool): Whether the request was successful.
        result (int): Result code of the operation.
        status (int): HTTP status code of the response.
        payment (PaymentConfirmDetails): Details of the payment.

    """

    success: bool
    result: int
    status: int
    payment: PaymentConfirmDetails
