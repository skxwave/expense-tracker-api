from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, MySQLDsn


class SuperUser(BaseModel):
    email: str
    password: str
    is_active: bool = True
    is_superuser: bool = True
    is_verified: bool = True


class Run(BaseModel):
    host: str = "localhost"
    port: int = 8000


class DatabaseSettings(BaseModel):
    url: MySQLDsn
    echo: bool = False
    echo_pool: bool = False
    max_overflow: int = 10


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_token_secret: str
    verification_token_secret: str


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    auth: str = "/auth"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()

    @property
    def bearer_token_url(self) -> str:
        parts = (self.prefix, self.v1.prefix, self.v1.auth)
        path = "".join(parts)
        return path[1:]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", ".env.template"),
        env_prefix="FASTAPI__",
        env_nested_delimiter="__",
        case_sensitive=False,
    )
    api: ApiPrefix = ApiPrefix()
    run: Run = Run()
    db: DatabaseSettings
    access_token: AccessToken
    superuser: SuperUser


settings = Settings()
