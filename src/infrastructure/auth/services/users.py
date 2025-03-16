from typing import Any

from litestar_users.service import BaseUserService

from src.infrastructure.database.models.users import User


class UserService(BaseUserService[User, Any]):
    pass
