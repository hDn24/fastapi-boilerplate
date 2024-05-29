from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str = Field(default="0.0.0.0")
    DB_PORT: int = Field(default=5432)
    DB_NAME: str = Field(default="db")
    DB_USER: str = Field(default="postgres")
    DB_PASS: str = Field(default="postgres")

    class Config:
        env_file = ".env"
        allow_mutation = False


settings = Settings()
