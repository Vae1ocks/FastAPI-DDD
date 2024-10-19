from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, RedisDsn

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class BaseSettingsConfig(BaseSettings):
    class Config:
        env_file = f"{BASE_DIR}/.env"
        extra = "ignore"


class DatabaseSettings(BaseSettingsConfig):
    @property
    def url(self) -> PostgresDsn:
        return (
            f"postgresql+asyncpg://{self.user}:{self.password}"
            f"@{self.host}:{self.port}/{self.name}"
        )

    echo: bool = False

    host: str
    port: str
    name: str
    user: str
    password: str

    class Config:
        env_prefix = "DB_"


class JWTSettings(BaseSettingsConfig):
    secret: str
    algorithm: str = "HS256"
    access_token_lifespan_minutes: str = 5
    refresh_token_lifespan_days: str = 15

    class Config:
        env_prefix = "JWT_"


class SessionSettings(BaseSettingsConfig):
    secret: str

    class Config:
        env_prefix = "SESSION_"


class RedisSettings(BaseSettingsConfig):
    port: str
    host: str

    @property
    def url(self) -> RedisDsn:
        return f"redis://{self.host}:{self.port}"

    class Config:
        env_prefix = "REDIS_"


class SMTPSettings(BaseSettingsConfig):
    host: str
    host_user: str
    host_password: str
    port: str

    class Config:
        env_prefix = "SMTP_"


class Settings(BaseSettings):
    db: DatabaseSettings = DatabaseSettings()
    jwt: JWTSettings = JWTSettings()
    session: SessionSettings = SessionSettings()
    redis: RedisSettings = RedisSettings()
    smtp: SMTPSettings = SMTPSettings()


settings = Settings()
