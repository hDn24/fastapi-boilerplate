import secrets

from pydantic import Field, PostgresDsn, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True, extra="ignore")

    DB_HOST: str = Field(default="0.0.0.0")
    DB_PORT: int = Field(default=5432)
    DB_NAME: str = Field(default="postgres")
    DB_USER: str = Field(default="postgres")
    DB_PASS: str = Field(default="postgres")

    API_V1_STR: str = Field(default="/api/v1")

    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=60 * 24 * 8)
    SECRET_KEY: str = Field(default=secrets.token_urlsafe(32))

    SUPER_USER: str = Field(examples="admin@example.com")
    SUPER_USER_PASSWORD: str = Field(examples="admin")

    @computed_field  # type: ignore[misc]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        """
        A property that returns the SQLALCHEMY_DATABASE_URI based on the DB_USER, DB_PASS, DB_HOST, DB_PORT, and DB_NAME attributes.
        Returns a PostgresDsn object.
        """
        return MultiHostUrl.build(
            scheme="postgresql+psycopg",
            username=self.DB_USER,
            password=self.DB_PASS,
            host=self.DB_HOST,
            port=self.DB_PORT,
            path=self.DB_NAME,
        )


settings = Settings()
