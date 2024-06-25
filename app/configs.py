import secrets

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str = Field(default="localhost")
    DB_PORT: int = Field(default=5432)
    DB_NAME: str = Field(default="postgres")
    DB_USER: str = Field(default="postgres")
    DB_PASS: str = Field(default="postgres")
    API_V1_STR: str = Field(default="/api/v1")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=60 * 24 * 8)
    SECRET_KEY: str = Field(default=secrets.token_urlsafe(32))

    class Config:
        env_file = ".env"
        # allow_mutation = False


settings = Settings()
