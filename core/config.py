from starlette.config import Config


class Settings:
    config = Config(".env")

    PROJECT_NAME: str = "Analys platform"
    PROJECT_VERSION: str = "0.0.1"

    DATABASE_URL = config("IA_DATABASE_URL", cast=str, default="")
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    SECRET_KEY = config("IA_SECRET_KEY", cast=str,
                        default="60fae8996bb10fe05285b261396333e64fb2a2b6d36b9f269d12f35aad5c6e97")
    ALGORITHM = "HS256"


settings = Settings()
