import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    API_TITLE: str = "Deprem Nerede Oldu API"
    API_V1_PREFIX: str = "/v1"
    ENV: str = os.getenv("ENV", "staging")
    API_KEY_HEADER_NAME: str = "x-api-key"
    API_KEY_GET: str = os.getenv("API_KEY_GET")
    API_KEY_POST: str = os.getenv("API_KEY_POST")
    FIRESTORE_CREDENTIALS_PATH_FOR_DEV: str = os.getenv("FIRESTORE_CREDENTIALS_FOR_DEV")
    COLLECTION_NAME: str = os.getenv("COLLECTION_NAME")
    DOCUMENT_NAME: str = os.getenv("DOCUMENT_NAME")
    NB_EARTHQUAKES_TO_STOCK_IN_FIRESTORE: int = 2000


settings = Settings()
