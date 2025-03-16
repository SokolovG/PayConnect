from litestar_users.adapter.sqlalchemy.mixins import SQLAlchemyUserMixin

from src.infrastructure.database.config import Base


class User(Base, SQLAlchemyUserMixin):
    pass
