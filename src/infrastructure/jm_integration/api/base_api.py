import logging

from src.infrastructure.jm_integration.client import JMClient


class BaseAPI:
    def __init__(self, client: JMClient) -> None:
        """Initialize Base API class.

        Args:
            client: async client for HTTP requests

        Instance Attributes:
            client: async client for HTTP requests
            base_url: prefix for all-endpoints
            payment_url: basic url with payment prefix for JMPaymentAPI
            payout_url: basic url with payout_url prefix for JMPayoutAPI
            refund_url: basic url with refund_url prefix for JMRefundAPI
            logger: logger for all api

        """
        self.client: JMClient = client
        self.base_url: str = "/api/v1/"
        self.payment_url = f"{self.base_url}/payments/"
        self.payout_url = f"{self.base_url}/payouts"
        self.refund_url = f"{self.base_url}/refunds"
        self.logger = logging.getLogger(self.__class__.__name__)
