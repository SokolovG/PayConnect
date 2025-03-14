from litestar import Controller


class PaymentController(Controller):
    path = "/payments"

    async def create_payment(self) -> None: ...
