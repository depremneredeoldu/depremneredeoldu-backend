from copy import deepcopy
from typing import Dict, List

from google.cloud import firestore_v1

from app.core.config import settings
from app.schemas.earthquake import EarthquakeModel


def get_earthquake(db: firestore_v1.client.Client, earthquake_id: str) -> list[dict]:
    document = db.collection(settings.COLLECTION_NAME).document(settings.DOCUMENT_NAME)
    document_dict = document.get().to_dict()
    all_earthquakes_list = document_dict.get("earthquakes_list")

    if all_earthquakes_list is None:
        return None

    for earthquake in all_earthquakes_list:
        if earthquake.get("earthquake_id") == earthquake_id:
            return earthquake
    return None


def get_earthquakes(db: firestore_v1.client.Client, limit: int) -> List[Dict[str, str]]:
    document = db.collection(settings.COLLECTION_NAME).document(settings.DOCUMENT_NAME)
    document_dict = document.get().to_dict()
    all_earthquakes_list = document_dict.get("earthquakes_list", [])

    if not all_earthquakes_list:
        return []

    # Filter desc
    all_earthquakes_list.sort(key=lambda item: item["earthquake_id"], reverse=True)

    if limit is None:
        return all_earthquakes_list

    return all_earthquakes_list[:limit]


def insert_earthquake(
    db: firestore_v1.client.Client, earthquake: EarthquakeModel
) -> None:
    document = db.collection(settings.COLLECTION_NAME).document(settings.DOCUMENT_NAME)
    document_dict = document.get().to_dict()
    all_earthquakes_list = document_dict.get("earthquakes_list", [])
    new_earthquakes_list = deepcopy(all_earthquakes_list)
    earthquake_dict = earthquake.model_dump()

    # Add earthquake in earthquake list
    new_earthquakes_list.append(earthquake_dict)

    # Filter desc
    new_earthquakes_list.sort(key=lambda item: item["earthquake_id"], reverse=True)

    # Update our array in firestore
    document.update(
        earthquakes=new_earthquakes_list[
            : settings.NB_EARTHQUAKES_TO_STOCK_IN_FIRESTORE
        ]
    )
