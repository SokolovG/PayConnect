from typing import Protocol, runtime_checkable

from src.payconnect.dto.schemas import Payload, Payment


@runtime_checkable
class JMPaymentAPI(Protocol):
    def get_payment(self, payment_id: str) -> Payment: ...
    def create_payment(self, payment_data: Payload) -> Payment: ...
