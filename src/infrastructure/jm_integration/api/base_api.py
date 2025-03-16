from src.infrastructure.jm_integration.client import JMClient


class BaseAPI:
    def __init__(self, client: JMClient) -> None:
        self.client: JMClient = client
        self.base_url: str = "/api/v1/"
