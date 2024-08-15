from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, MySQLDsn


class Run(BaseModel):
    host: str = "localhost"
    port: int = 8000


class DatabaseSettings(BaseModel):
    url: MySQLDsn
    echo: bool = True
    echo_pool: bool = False
    max_overflow: int = 10


class ApiPrefix(BaseModel):
    pass


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", ".env.template"),
        env_prefix="FASTAPI__",
        env_nested_delimiter="__",
        case_sensitive=False,
    )
    db: DatabaseSettings
    run: Run = Run()


settings = Settings()
