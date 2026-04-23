from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    database_url: str = Field(alias="DATABASE_URL")
    jwt_secret_key: str = Field(alias="JWT_SECRET_KEY")
    jwt_algorithm: str = Field(default="HS256", alias="JWT_ALGORITHM")
    access_token_expire_minutes: int = Field(default=5, alias="ACCESS_TOKEN_EXPIRE_MINUTES")
    refresh_token_expire_days: int = Field(default=5, alias="REFRESH_TOKEN_EXPIRE_DAYS")
    admin_email: str = Field(alias="ADMIN_EMAIL")
    admin_password: str = Field(alias="ADMIN_PASSWORD")
    admin_name: str = Field(default="System Admin", alias="ADMIN_NAME")
    cors_origins: list[str] = Field(default_factory=lambda: ["http://localhost:5173"], alias="CORS_ORIGINS")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
