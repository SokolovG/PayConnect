from litestar import Router

from src.interfaces.api.controllers.payment_controller import PaymentController

event_router = Router(path="/api", route_handlers=[PaymentController])
