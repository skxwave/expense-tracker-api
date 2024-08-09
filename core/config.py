from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, MySQLDsn


class DatabaseSettings(BaseModel):
    url: MySQLDsn


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


settings = Settings()
