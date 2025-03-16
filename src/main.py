import uvicorn
from litestar import Litestar
from litestar_users import LitestarUsersPlugin
from sqladmin_litestar_plugin import SQLAdminPlugin

from src.infrastructure.auth.get_users_config import litestar_users_config
from src.infrastructure.database.config import (
    get_sqlalchemy_config,
    get_sqlalchemy_plugin,
)
from src.infrastructure.logging.config import logging_config
from src.interfaces.cli.commands import CLIPlugin

sqlalchemy_plugin = get_sqlalchemy_plugin()
sqlalchemy_config = get_sqlalchemy_config()
admin = SQLAdminPlugin(engine=sqlalchemy_config.get_engine(), base_url="/admin", views=[])

litestar_users = LitestarUsersPlugin(config=litestar_users_config)
app = Litestar(
    route_handlers=[],
    plugins=[sqlalchemy_plugin, admin, CLIPlugin(), litestar_users],
    debug=True,
    logging_config=logging_config,
)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
