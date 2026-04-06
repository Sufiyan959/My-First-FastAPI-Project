from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import ValidationError
import sys


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    DB_CONNECTION: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int


try:
    settings = Settings()
except ValidationError as e:
    print("\n Error: Missing required environment variables in .env file:")
    for error in e.errors():
        print(f"{error['loc'][0]}: {error['msg']}")
    print("\nPlease create .env file with required variables.\n")
    sys.exit(1)
