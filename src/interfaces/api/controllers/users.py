from litestar import Controller, get

from src.domain.dto.base import ReturnUser, ReturnUserDTO, User, UserDTO


class UserController(Controller):
    path = "/users"
    dto = UserDTO
    return_dto = ReturnUserDTO
    @get()
    def get_users(self) -> list[ReturnUser]:
        users = [User(name="Алексей"), User(name="Мария")]
        return [ReturnUser(name=user.name) for user in users]