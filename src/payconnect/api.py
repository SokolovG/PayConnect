from src.payconnect.client import JMClient
from src.payconnect.dto.schemas import Payload, Payment
from src.payconnect.enums import HttpMethod


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
            json=payment_data,
            response_type=Payment,
        )
