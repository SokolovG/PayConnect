import os
from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


class JMSettings(BaseSettings):
    JM_TOKEN: str = os.environ.get("JM_TOKEN")


jm_settings = JMSettings()
