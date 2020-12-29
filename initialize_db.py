from app import app
from db import db
from config import data_txt_name
from extract_data import extract_from_web, clean_data_extracted, create_dict
from models.earthquake import EarthquakeModel


def create_tables(data_json):
    with app.app_context():
        db.init_app(app)
        db.drop_all()
        db.create_all()

        for data in data_json:
            earthquake = EarthquakeModel(**data)
            earthquake.save_to_db()


if __name__ == "__main__":
    # extract data from web
    extract_from_web(file_name=data_txt_name)

    # clean the whitespace and structure data
    clean_data_extracted(file_name=data_txt_name)

    # convert txt file to json structure
    all_data_json = create_dict(file_name=data_txt_name)

    # create db from json
    create_tables(all_data_json)




