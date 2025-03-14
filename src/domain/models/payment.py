from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from src.infrastructure.jm_integration.enums import Status


@dataclass
class Payment:
    amount: Decimal
    currency: str
    status: Status
    description: str = None
    id: str = None
    external_id: str = None
    created_at: datetime = None
    updated_at: datetime = None

    def update_status(self, new_status: Status) -> None:
        self.status = new_status
