# DepremNeredeOldu: The earthquakes visualization

For this project, I used **Python** on the backend (**Flask RESTful API**). The goal is to visualize the earthquakes in Turkey on map with [MapBox](https://www.mapbox.com). The project is deployed on [depremneredeoldu.com](https://depremneredeoldu.com)

# Requirements

##### Create a new virtual environment
    python3 -m venv venv

###### And then,

    pip install -r requirements.txt

# To run

##### Initialize the database before to run.

    python initialize_db.py

##### And then,

    python app.py

# Automate your data extraction

If you want to update earthquake data automatically, you can use **CRON** to automate this processus by executing **initialize_db.py**


## Data

The data comes from **Kandilli Observatory and Earthquake Research Institute** and cannot be used for commercial purposes in any way without the written permission and approval of **Boğaziçi University**.


## Contact

    Alican Yüksel - alicanyuksel@outlookcom