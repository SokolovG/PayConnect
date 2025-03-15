from msgspec import Struct


class CommissionData(Struct):
    """Data on the payment commission."""

    commission_value: float
    commission_fee: float
    commission_amount: float
