import pathlib
from typing import Optional

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent


class Telegraph(BaseModel):
    short_name: str
    author_name: str
    author_url: str
    access_token: str


class Tokens(BaseModel):
    telegram: str
    mistral: str
    secret: str
    graspil: str


class Admins(BaseModel):
    ids: list[int]


class LoggerConfig(BaseModel):
    level: str


class Host(BaseModel):
    address: str


class DatabaseConfig(BaseModel):
    host: str
    port: int
    user: str
    pwd: str
    name: str
    url: Optional[str] = None
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 5
    max_overflow: int = 10

    def model_post_init(self, __context: dict) -> None:
        if self.url is None:
            self.url = (
                f"postgresql+asyncpg://{self.user}:"
                f"{self.pwd}@{self.host}:"
                f"{self.port}/{self.name}"
            )


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
    db: DatabaseConfig
    admins: Admins
    telegraph: Telegraph


settings = Settings()
