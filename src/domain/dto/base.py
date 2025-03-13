from uuid import UUID, uuid4

from litestar.dto import DTOConfig, MsgspecDTO
from msgspec import Struct, field


class User(Struct):
    name: str
    id: UUID = field(default_factory=uuid4)

class ReturnUser(Struct):
    name: str


class UserDTO(MsgspecDTO[User]):
    config = DTOConfig(exclude={"id"})

class ReturnUserDTO(MsgspecDTO[ReturnUser]):
    config = DTOConfig(exclude={"id"})