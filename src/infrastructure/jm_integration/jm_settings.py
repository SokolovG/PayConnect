from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


class JMSettings(BaseSettings):
    JM_TOKEN: str

    class Config:
        env_file = ".jm_env"
        env_file_encoding = "utf-8"


jm_settings = JMSettings()
