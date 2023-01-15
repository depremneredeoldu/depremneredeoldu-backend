import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    API_TITLE: str = "Deprem Nerede Oldu API"
    ENV: str = os.getenv("ENV", "staging")
    API_KEY_HEADER_NAME: str = "x-api-key"
    API_KEY: str = os.getenv("API_KEY")


settings = Settings()
