import secrets
import warnings

from pydantic import Field, PostgresDsn, computed_field, model_validator
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict  # type: ignore
from typing_extensions import Self


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True, extra="ignore")

    ENVIRONMENT: str = Field(default="local")
    PROJECT_NAME: str = Field(default="fastapi-boilerplate")

    DB_HOST: str = Field(default="0.0.0.0")
    DB_PORT: int = Field(default=5432)
    DB_NAME: str = Field(default="postgres")
    DB_USER: str = Field(default="postgres")
    DB_PASS: str = Field(default="postgres")

    API_V1_STR: str = Field(default="/api/v1")

    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=60 * 24 * 8)
    SECRET_KEY: str = Field(default=secrets.token_urlsafe(32))

    SUPER_USER: str = Field(default="hDn24@gmail.com", examples=["hDn24@gmail.com"])
    SUPER_USER_PASSWORD: str = Field(default="changethis", examples=["hDn24"])

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

    def _check_default_secret(self, var_name: str, value: str | None) -> None:
        """
        A function that checks the default value of a secret variable and issues a warning if it is set to "changethis".

        Args:
            var_name: The name of the variable being checked.
            value: The value of the variable being checked.

        Returns:
            None
        """
        if value == "changethis":
            message = (
                f'The value of {var_name} is "changethis", ' "for security, please change it, at least for deployments."
            )
            if self.ENVIRONMENT == "local":
                warnings.warn(message, stacklevel=1)
            else:
                raise ValueError(message)

    @model_validator(mode="after")
    def _enforce_non_default_secrets(self) -> Self:
        """
        Enforces that the values of `SECRET_KEY`, `DB_PASS`, and `SUPERUSER_PASSWORD` are not set to their default values.
        """
        self._check_default_secret("SECRET_KEY", self.SECRET_KEY)
        self._check_default_secret("DB_PASS", self.DB_PASS)
        self._check_default_secret("SUPERUSER_PASSWORD", self.SUPER_USER_PASSWORD)

        return self


settings = Settings()
