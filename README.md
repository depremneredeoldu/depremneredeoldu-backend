# DepremNeredeOldu: Backend

For this project, I used **Python** on the backend (**Flask RESTful API**). The goal is to build the Earthquake API which gives you the earthquakes informations in Turkey. To do that, we get the data unstructured with web scraping and structure them into json structure and write them on the database.

The project is deployed on [depremneredeoldu.com](https://depremneredeoldu.com) with Nginx on Ubuntu server. The backend URL is [api.depremneredeoldu.com](https://api.depremneredeoldu.com)


## Requirements

    pip install -r requirements.txt

## Initialize the database

    python initialize_db.py

## To run

    python app.py

## Automate your data extraction

If you want to update the earthquake data automatically, you can configure a **Cron Job** to automate this processus by executing **initialize_db.py** script every minute.

## Data

The data comes from **Kandilli Observatory and Earthquake Research Institute** and cannot be used for commercial purposes in any way without the written permission and approval of **Boğaziçi University**.

## Contact

    Alican Yüksel - alicanyuksel@outlook.com