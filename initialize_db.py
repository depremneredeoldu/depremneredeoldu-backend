from config import data_txt_name
from extract_data import extract_from_web, clean_data_extracted, create_dict
import requests
import os
from dotenv import load_dotenv
load_dotenv()

URL_GET_BACKEND_PROD = os.getenv("URL_GET_API_BACKEND_PROD")
URL_POST_BACKEND_PROD = os.getenv("URL_POST_API_BACKEND_PROD")

def get_all_earthquakes(url):
    r = requests.get(url)

    response = r.json()

    all_earthquakes = response["earthquakes"]

    all_earthquakes_id = []
    for earthquake in all_earthquakes:
        all_earthquakes_id.append(earthquake["earthquake_id"])

    return all_earthquakes_id


def save_to_db(data, url):
    all_earthquakes_list = get_all_earthquakes(url=URL_GET_BACKEND_PROD)

    for earthquake in data:
        earthquake_id = earthquake["earthquake_id"]
        # check if a new earthquake exists
        if earthquake_id not in all_earthquakes_list:
            r_post = requests.post(url, json=earthquake)


if __name__ == "__main__":
    # extract data from web
    extract_from_web(file_name=data_txt_name)

    # clean the whitespace and structure data
    clean_data_extracted(file_name=data_txt_name)

    # convert txt file to json structure
    all_data_json = create_dict(file_name=data_txt_name)

    # create db from json
    save_to_db(data=all_data_json, url=URL_POST_BACKEND_PROD)
