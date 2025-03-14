import msgspec

from src.interfaces.jm_integration.client import JMClient
from src.interfaces.jm_integration.enums import HttpMethod
from src.payconnect.dto.schemas import Payload, Payment


class JMPaymentAPI:
    def __init__(self, client: JMClient) -> None:
        self.client: JMClient = client

    def get_payment(self, payment_id: str) -> Payment:
        return self.client._make_request(
            method=HttpMethod.GET,
            endpoint=f"/api/v1/payments/{payment_id}",
            response_type=Payment,
        )

    def create_payment(self, payment_data: Payload) -> Payment:
        return self.client._make_request(
            method=HttpMethod.POST,
            endpoint="/api/v1/payments",
            json=msgspec.structs.asdict(payment_data),
            response_type=Payment,
        )
