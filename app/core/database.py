import firebase_admin
from firebase_admin import credentials, firestore

from app.core.config import settings


def get_firestore_db_object():
    if settings.ENV == "dev":
        cred = credentials.Certificate(settings.FIRESTORE_CREDENTIALS_PATH_FOR_DEV)
        try:
            app = firebase_admin.initialize_app(cred)
        except ValueError:
            app = firebase_admin.get_app()

        return firestore.client()

    try:
        app = firebase_admin.initialize_app()
    except ValueError:
        app = firebase_admin.get_app()

    return firestore.client()
