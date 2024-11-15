import sys

from pydantic_settings import SettingsConfigDict, BaseSettings
from pathlib import Path


class Setting(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    JWT_KEY: str
    ALGORITHM: str


    @property
    def async_DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=str(Path(__file__).parent.parent / ".env"))

setting = Setting()
