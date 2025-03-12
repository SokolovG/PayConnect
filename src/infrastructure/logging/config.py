from litestar.logging import LoggingConfig

logging_config = LoggingConfig(
    root={"level": "INFO", "handlers": ["queue_listener"]},
    formatters={
        "standard": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"},
    },
    loggers={
        "src.main": {"level": "DEBUG", "propagate": True},
    },
    log_exceptions="always",
)