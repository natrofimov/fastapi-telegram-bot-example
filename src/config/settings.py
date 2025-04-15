import pathlib

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent


class Tokens(BaseModel):
    telegram: str

class Admins(BaseModel):
    ids: list[int]

class LoggerConfig(BaseModel):
    level: str

class Host(BaseModel):
    address: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="BOT__",
    )
    logger: LoggerConfig
    tokens: Tokens
    host: Host
    admins: Admins


settings = Settings()
