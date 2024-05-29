from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_host: str = Field(default="0.0.0.0")
    db_port: int = Field(default=5432)
    db_name: str = Field(default="db")
    db_user: str = Field(default="postgres")
    db_pass: str = Field(default="postgres")
    sqlalchemy_echo: bool = Field(default=False)

    class Config:
        env_file = ".env"
        allow_mutation = False


settings = Settings()
