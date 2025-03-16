from litestar.security.jwt import JWTAuth
from litestar_users import LitestarUsersConfig
from litestar_users.config import (
    AuthHandlerConfig,
    RegisterHandlerConfig,
    VerificationHandlerConfig,
)

from src.infrastructure.auth.dto import UserReadDTO, UserRegistrationDTO, UserUpdateDTO
from src.infrastructure.auth.services import UserService
from src.infrastructure.database.models.users import User

litestar_users_config = LitestarUsersConfig(
    auth_backend_class=JWTAuth,
    secret="",
    user_model=User,  # noqa
    user_read_dto=UserReadDTO,
    user_registration_dto=UserRegistrationDTO,
    user_update_dto=UserUpdateDTO,
    user_service_class=UserService,  # noqa
    auth_handler_config=AuthHandlerConfig(),
    register_handler_config=RegisterHandlerConfig(),
    verification_handler_config=VerificationHandlerConfig(),
)
