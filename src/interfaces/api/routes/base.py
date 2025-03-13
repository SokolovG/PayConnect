from litestar import Router

from src.interfaces.api.controllers.users import UserController

event_router = Router(
    path="/api",
    route_handlers=[UserController]
)
