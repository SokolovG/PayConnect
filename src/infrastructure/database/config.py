from advanced_alchemy.base import UUIDBase
from litestar.contrib.sqlalchemy.plugins import (
    SQLAlchemyAsyncConfig,
    SQLAlchemyPlugin,
)
from sqlalchemy import MetaData

from src.infrastructure.database.settings import settings


class Base(UUIDBase):
    """Basic config for all models SQLAlchemy Naming Convention Dictionary.

    Include UUID ID

    "ix": "ix_%(column_0_label)s"
    Format for indexes.
    "uq": "uq_%(table_name)s_%(column_0_name)s"
       Format for unique constraints.
    "ck": "ck_%(table_name)s_%(constraint_name)s"
       Format for check constraints.
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"
       Format for foreign keys.
    "pk": "pk_%(table_name)s"
       Format for primary keys.
    """

    __abstract__ = True
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )


def get_sqlalchemy_config() -> SQLAlchemyAsyncConfig:
    """Return SQLAlchemy config for SQLAlchemyPlugin."""
    return SQLAlchemyAsyncConfig(
        connection_string=settings.database_url, create_all=True, metadata=Base.metadata
    )


def get_sqlalchemy_plugin() -> SQLAlchemyPlugin:
    """Return SQLAlchemy plugin for Litestar."""
    return SQLAlchemyPlugin(config=get_sqlalchemy_config())
