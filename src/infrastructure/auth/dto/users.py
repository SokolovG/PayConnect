from dataclasses import dataclass

from advanced_alchemy.extensions.litestar.dto import SQLAlchemyDTO, SQLAlchemyDTOConfig
from litestar.dto import DataclassDTO

from src.infrastructure.database.models.users import User


@dataclass
class UserRegistrationSchema:
    email: str
    password: str


class UserRegistrationDTO(DataclassDTO[UserRegistrationSchema]):
    """DTO for user registration."""


class UserReadDTO(SQLAlchemyDTO[User]):
    """DTO for reading user data."""

    config = SQLAlchemyDTOConfig()


class UserUpdateDTO(SQLAlchemyDTO[User]):
    """DTO for updating user data."""

    config = SQLAlchemyDTOConfig(partial=True)
